import pandas as pd
import json
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.dates as mdates
import matplotlib.font_manager
import numpy as np

def process_data(df):
    # 使用pivot_table重塑数据
    df_pivot = df.pivot_table(index=['车号', '日期'],
                              columns='部门',
                              values=['已完成数量', '未完成数量'],
                              aggfunc='sum')

    # 将MultiIndex的第二层堆叠为长格式数据
    df_stacked = df_pivot.stack().reset_index()
    # print(f"将MultiIndex的第二层堆叠为长格式数据df_stacked: \n{df_stacked}")
    
    # 将堆叠后的索引转换为列，保留所有索引级别
    df_stacked.columns = ['车号', '日期', '部门', '已完成数量', '未完成数量']

    # 检查'日期'列的数据类型，如果需要则转换为datetime类型
    if not np.issubdtype(df_stacked['日期'].dtype, np.datetime64):
        df_stacked['日期'] = pd.to_datetime(df_stacked['日期'], infer_datetime_format=True, errors='coerce')


    # 现在df_stacked应该有'车号'、'日期'、'部门'、'已完成数量'和'未完成数量'五列
    # print(f"df_stacked: \n{df_stacked}")
    return df_stacked


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.lines import Line2D

def plot_data(df_stacked, train_consist):
    car_number_to_index = {car_number: int(index) for index, car_number in enumerate(df_stacked['车号'].unique())}
    # print(f"car_number_to_index: \n{car_number_to_index}")
    df_stacked['车号_index'] = df_stacked['车号'].map(car_number_to_index)
    # print(f"df_stacked: \n{df_stacked}")

    
    # 部门颜色列表，使用浅色调
    colors = [
        'lightblue',       # 浅蓝色
        'lightcoral',      # 浅珊瑚色
        'lightgreen',      # 浅绿色
        'lightcyan',       # 浅青色
        'orchid',          # 淡紫色
        'lightsalmon',     # 浅鲑鱼色
        'palegoldenrod',   # 淡金色
        'slategrey',       # 青灰色
        'thistle',         # 苔色
        'plum',            # 梅色
        'lightseagreen',   # 浅海绿色
        'skyblue',         # 天蓝色
        'palevioletred',   # 淡紫红色
        'lightsteelblue',  # 浅钢蓝色
        'lightgrey'        # 浅灰色
    ]

    unique_dates = df_stacked['日期'].unique()
    latest_date = unique_dates[-1]  # 最近的日期
    latest_data = df_stacked[df_stacked['日期'] == latest_date]

    num_cars = len(car_number_to_index)
    num_subplots = int(np.ceil(num_cars / train_consist))
    fig, axs = plt.subplots(nrows=num_subplots, figsize=(10, 3*num_subplots))

    if not isinstance(axs, np.ndarray):
        axs = [axs]

    for i, ax in enumerate(axs):
        start_index = int(i * train_consist)
        end_index = int(min((i + 1) * train_consist, num_cars))
        subset_data = latest_data[latest_data['车号_index'].between(start_index, end_index-1)]

        ax.set_title(f"日期：{latest_date.strftime('%Y%m%d')} 车号 :{list(car_number_to_index.keys())[start_index]} 到 {list(car_number_to_index.keys())[end_index-1]}")
        ax.set_ylabel('数量')

        # 初始化x位置和底部累积值
        x_positions = np.arange(start_index, end_index)
        bottom_values = np.zeros(len(x_positions))

        # 循环遍历每个部门，绘制堆积条形图
        for department in df_stacked['部门'].unique():
            dept_data = subset_data[subset_data['部门'] == department]
            completed_counts = dept_data['已完成数量'].values
            uncompleted_counts = dept_data['未完成数量'].values
            total_counts = completed_counts + uncompleted_counts

            # 使用映射找到颜色索引
            color_index = list(df_stacked['部门'].unique()).index(department)

            # 绘制堆积条形图
            ax.bar(x_positions, total_counts, bottom=bottom_values, width=0.8, align='center',
                   color=colors[color_index], label=f"{department}")

            # 更新底部累积值
            bottom_values += total_counts

            # 添加数据标签
            for car_index in range(start_index, end_index):
                ax.text(x_positions[car_index-start_index], bottom_values[car_index-start_index] - total_counts[car_index-start_index]/2,
                        f"{completed_counts[car_index-start_index]} / {uncompleted_counts[car_index-start_index]}",
                        ha='center', va='center')

        # 设置x轴刻度和标签
        ax.set_xticks(x_positions)
        ax.set_xticklabels(list(car_number_to_index.keys())[start_index:end_index], rotation=90)

        # 添加图例
        ax.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(f"stacked_bar_charts_{datetime.now().strftime('%Y%m%d%H%M%S')}.png", dpi=100)








# 设置matplotlib字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 获取当前日期并格式化为年月日形式
current_datetime = datetime.now().strftime('%Y%m%d %H-%M')
# 加载数据
book_name = '巴西圣保罗项目单轨项目CIB执行管理台账'
with open('history.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    history_data = data.get(f"{book_name}history", {})

    train_consist=data[book_name]["train_consist"]

    # 创建一个空列表，用于存储扁平化的数据
    flat_history = []

    # 遍历历史数据
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

# 将扁平化的数据转换为DataFrame
df_history = pd.DataFrame(flat_history)





# 确保'日期'列是datetime类型
df_history['日期'] = pd.to_datetime(df_history['日期'], format="%Y年%m月%d日", errors='coerce')


df_povit = process_data(df_history)

plot_data(df_povit,train_consist)
