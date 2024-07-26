# -*- coding: utf-8 -*-
import pandas as pd

# import openpyxl
import os
import json
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
# 获取当前日期并格式化为年月日形式
current_datetime = datetime.now().strftime('%Y%m%d %H-%M')
# 设置matplotlib字体以支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 以微软雅黑为例
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
book_name='吉隆坡机场APM300R项目CIB执行管理台账'

def main():
    # 对history.json的存储数据进行删除记录并进行扁平化转化为DataFrame.
    with open('history.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for ts, ts_data in data[f"{book_name}history"].items():

            # 处理历史记录,将date数据多余的数据进行删除
            data[f"{book_name}"][ts] = process_history(data[f"{book_name}history"][ts])
        
        history_data = data[f"{book_name}history"]
        
        # 创建一个空列表，用于存储扁平化的数据
        flat_history = []

        # 遍历 history 数据
        for ts, ts_data in history_data.items():            
            for date, date_data in ts_data.items():
                for car_type, car_type_data in date_data.items():
                    for car, car_data in car_type_data.items():
                        
                        completed_count = car_data["已完成数量"]
                        remaining_count = car_data["未完成数量"]
                        # car_dep=[line.split("\n") for line in car.strip().splitlines()]
                        data1, data2 = car.split('\n')
                        flat_history.append({
                            "车号": data1,
                            "部门": data2,
                            "日期": date,
                            "已完成数量": completed_count,
                            "未完成数量": remaining_count
                        })

        # 将扁平化的数据转换为 DataFrame
        df_history = pd.DataFrame(flat_history)



    # 保存更新后的 Json 数据

    with open('history.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    #     print(f"history.json 文件更新成功.\n接下来，将历史数据更新到{excel_file_name}文件中")
     
    # append_df_to_excel(df_history, excel_file_name, sheet_name=f"history")          

    # 将日期列转换为日期时间格式
    df_history['日期'] = pd.to_datetime(df_history['日期'], format="%Y年%m月%d日", dayfirst=True)



    # 将数据重塑为长格式，以便于绘图
    df_long = pd.melt(df_history, id_vars=['车号', '部门', '日期'],
                    value_vars=['已完成数量', '未完成数量'],
                    var_name='状态', value_name='数量')

    # 设置图形大小
    plt.figure(figsize=(14, 8))

    # 使用catplot绘制分组条形图
    g = sns.catplot(x='日期', y='数量', hue='状态', col='部门',
                    data=df_long, kind="bar",
                    height=6, aspect=.7, palette="Set2")

    # 添加标题和轴标签
    g.set_axis_labels("日期", "数量")
    g.set_titles("{col_name}")

    # 添加数值标签
    for ax in g.axes.flatten():
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # 调整布局，防止标签被截断
    plt.tight_layout()

    # 显示图表
    plt.show()
    
    # 保存图表到文件
    plt.savefig(f'output.png', dpi=300)
    print(f"图表已保存到output_{current_datetime}.png")

  

def process_history(history_data):
    # 获取历史记录的键（即日期）
    dates = sorted(history_data.keys())

    while len(dates) > 30:
        oldest_date = dates.pop(0)
        del history_data[oldest_date]
        print(f"历史内容过多，历史记录中{oldest_date}的记录被删除")    
    return history_data


if __name__ =='__main__':
    main()

