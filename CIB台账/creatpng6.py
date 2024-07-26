import pandas as pd
import json
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 移除重复的导入语句，优化代码结构
# 设置matplotlib字体以支持中文，移到适当的位置以确保其在绘图前被配置

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用微软雅黑字体支持中文
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def process_data(df):
    try:
        # 使用pivot_table重塑数据
        df_pivot = df.pivot_table(
            index=['车号', '日期'],
            columns='部门',
            values=['已完成数量', '未完成数量'],
            aggfunc='sum'
        )

        # 将MultiIndex的第二层堆叠为长格式数据，使用新的stack()行为
        df_stacked = df_pivot.stack(future_stack=True).reset_index()
        
        # 将堆叠后的索引转换为列，保留所有索引级别
        df_stacked.columns = ['车号', '日期', '部门', '已完成数量', '未完成数量']

        # 检查'日期'列的数据类型，如果需要则转换为datetime类型
        if not np.issubdtype(df_stacked['日期'].dtype, np.datetime64):
            df_stacked['日期'] = pd.to_datetime(df_stacked['日期'], errors='coerce')
    except Exception as e:
        print(f"数据处理出错：{e}")
        raise

    return df_stacked

def plot_data(df_stacked, train_consist, colors):
    car_number_to_index = {car_number: int(index) for index, car_number in enumerate(df_stacked['车号'].unique())}
    df_stacked['车号_index'] = df_stacked['车号'].map(car_number_to_index)
    if train_consist<3:
        t=6
    else:
        t=train_consist
    unique_dates = df_stacked['日期'].unique()
    latest_date = unique_dates[-1]
    previous_date = unique_dates[-2]

    date_colors = {
        latest_date: 'orchid',  
        previous_date: 'lightgrey' 
    }

    num_cars = len(car_number_to_index)
    num_subplots = int(np.ceil(num_cars / t))
    fig, axs = plt.subplots(nrows=num_subplots, figsize=(10, 3*num_subplots))

    if not isinstance(axs, np.ndarray):
        axs = [axs]

    for i, ax in enumerate(axs):
        start_index = int(i * t)
        end_index = int(min((i + 1) * t, num_cars))
        subset_data = df_stacked[df_stacked['车号_index'].between(start_index, end_index-1)]

        ax.set_title(f"日期：{previous_date.strftime('%Y%m%d')}[浅灰色]和{latest_date.strftime('%Y%m%d')}[淡紫色]  车号 :{list(car_number_to_index.keys())[start_index]} 到 {list(car_number_to_index.keys())[end_index-1]}")
        ax.set_ylabel('数量')

        x_positions = np.arange(start_index, end_index)

        for date, x_pos in zip([previous_date, latest_date], [x_positions - 0.2, x_positions + 0.2]):
            day_data = subset_data[subset_data['日期'] == date]

            bottom_values = np.zeros(len(x_pos))

            for department in df_stacked['部门'].unique():
                dept_data = day_data[day_data['部门'] == department]
                completed_counts = dept_data['已完成数量'].values
                uncompleted_counts = dept_data['未完成数量'].values
                total_counts = completed_counts + uncompleted_counts

                color_index = list(df_stacked['部门'].unique()).index(department)
                dept_color = colors[color_index]

                bars = ax.bar(x_pos, total_counts, bottom=bottom_values, width=0.4, align='center',
                              color=dept_color, edgecolor=date_colors[date], label=f"{department} ({date.strftime('%Y%m%d')})")

                bottom_values += total_counts

                for bar, cc, uc in zip(bars, completed_counts, uncompleted_counts):
                    height = bar.get_height()
                    center_y = bar.get_y() + height / 2
                    ax.annotate(f'{cc}/{uc}', xy=(bar.get_x() + bar.get_width() / 2, center_y),
                                xytext=(0, 0), textcoords="offset points",
                                ha='center', va='center')

        ax.set_xticks(x_positions)
        ax.set_xticklabels(list(car_number_to_index.keys())[start_index:end_index], rotation=90)

        handles, labels = ax.get_legend_handles_labels()
        unique_labels = set()
        good_handles = []
        good_labels = []

        for handle, label in zip(handles, labels):
            department = label.split(' ')[0]
            if department not in unique_labels:
                good_handles.append(handle)
                good_labels.append(department)
                unique_labels.add(department)

        ax.legend(good_handles, good_labels, loc='upper center', bbox_to_anchor=(0.5, 1.05),
                  fancybox=True, shadow=True, ncol=len(good_labels))
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.savefig(f"stacked_bar_charts_{datetime.now().strftime('%Y%m%d%H%M%S')}.png", dpi=100)

if __name__ == "__main__":
    current_datetime = datetime.now().strftime('%Y%m%d %H-%M')
    book_name = '新加坡APM300RCIB执行管理台账'
    with open('history.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        history_data = data.get(f"{book_name}history", {})
        train_consist = data[book_name]["train_consist"]

        flat_history = []
        for ts, ts_data in history_data.items():
            for date, date_data in ts_data.items():
                for car_type, car_type_data in date_data.items():
                    for car, car_data in car_type_data.items():
                        completed_count = car_data["已完成数量"]
                        remaining_count = car_data["未完成数量"]
                        data1, data2 = car.split('\n')
                        flat_history.append({
                            "车号": data1,
                            "部门": data2,
                            "日期": date,
                            "已完成数量": completed_count,
                            "未完成数量": remaining_count
                        })

        df_history = pd.DataFrame(flat_history)
        df_history['日期'] = pd.to_datetime(df_history['日期'], format="%Y年%m月%d日", errors='coerce')
        df_povit = process_data(df_history)
        plot_data(df_povit, train_consist, colors=['lightblue', 'lightcoral', 'lightgreen', 'lightcyan', 'orchid',
                                                   'lightsalmon', 'palegoldenrod', 'slategrey', 'thistle', 'plum',
                                                   'lightseagreen', 'skyblue', 'palevioletred', 'lightsteelblue',
                                                   'lightgrey'])