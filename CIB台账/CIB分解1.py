# 导入tkinter模块用于创建简单的图形用户界面
import tkinter as tk
# 导入filedialog模块，用于打开文件对话框
from tkinter import filedialog
# 导入pandas模块，用于处理数据
import pandas as pd
# 导入xlwings模块，用于与Excel交互
import xlwings as xw

# 定义一个函数，用于选择并打开Excel文件
# 获取文件地址
file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel Files", "*.xlsx;*.xls")])
# 使用xlwings打开选择的Excel文件
wb = xw.Book(file_path)
# --------------OPEN-----------------------------def select_and_open_excel():
    # 创建一个Tkinter窗口并隐藏它
def select_and_open_excel():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 弹出文件选择对话框并获取用户选择的文件路径
    # file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel Files", "*.xlsx;*.xls")])
    
    # 如果用户选择了文件
    if file_path:  # 如果用户选择了文件
        # 打印已成功打开的文件路径
        # 使用xlwings打开选择的Excel文件
        # wb = xw.Book(file_path)
        print(f"已成功打开文件：{file_path}")
    
    # 关闭Tkinter窗口
    root.destroy()  # 关闭Tkinter窗口

# 调用函数打开Excel文件
# 调用函数
select_and_open_excel()

# 获取工作簿中的第一个工作表
sht1 = wb.sheets('Sheet1')
# 定义Dataframe1的标题区域范围
header1_range = 'A6:S6'  # Dataframe1的标题区域
# 定义Dataframe2的标题区域范围
header2_range = 'Z9:AJ9'  # Dataframe2的标题区域
# -----------get data----------------------------------
def get_data_from_range(sheet, header_range, start_col_num, end_col_num):
    """
    从指定的工作表中获取数据并转换为DataFrame。
    
    参数:
    sheet: xlwings中的工作表对象。
    header_range: 标题区域的范围。
    start_col_num: 数据起始列的编号。
    end_col_num: 数据结束列的编号。
    
    返回:
    DataFrame: 从Excel中提取的数据。
    """
    # 将列编号转换为列字母
    # 将列数转换为列字母
    start_col = xw.utils.col_name(start_col_num)
    end_col = xw.utils.col_name(end_col_num)
    
    # 获取标题行的数据
    # 获取标题，合并单元格中的值会被展开为重复值
    headers = sheet.range(header_range).value
    # 确定数据范围，从第十行开始扩展到最后的非空单元格
    start_row = 10
    last_row = sheet.cells.last_cell.row
    end_row = sheet.range(f'{end_col}{last_row}').end('up').row
    data_range = sheet.range(f'{start_col}{start_row}:{end_col}{end_row}')
    
    # 读取数据范围内的所有数据
    # 读取数据
    data = data_range.value
    
    # 将数据转换为DataFrame，并使用标题行作为列名
    # 转换为DataFrame
    df = pd.DataFrame(data, columns=headers[:len(data[0])])  # 根据实际读取的列数确定列数
    
    # 删除所有列都为空的行
    # 清除空行
    df = df.dropna(how='all')  # 删除所有列都为空的行
    
    return df

# 使用定义的函数从Sheet1中提取Dataframe1区域的数据
# 读取Dataframe1区域的数据，A列对应第1列，S列对应第19列
df1 = get_data_from_range(sht1, header1_range, 1, 19)
# 使用定义的函数从Sheet1中提取Dataframe2区域的数据
# 读取Dataframe2区域的数据，Z列对应第26列，AJ列对应第36列
df2 = get_data_from_range(sht1, header2_range, 26, 36)
# 将两个DataFrame合并为一个
# 以 A 列的值作为键名进行合并
merged_df = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)], axis=1)

# 检查是否存在名为"1车"的工作表，存在则删除
# 将merged_df数据存储到新的工作表"1车"中
new_sheet_name = "1车"

if new_sheet_name in [sheet.name for sheet in wb.sheets]:
    wb.sheets[new_sheet_name].delete()
# 创建一个新的工作表
wb.sheets.add(new_sheet_name)  # 添加新的工作表
# 将合并后的DataFrame写入新的工作表
new_sheet = wb.sheets[new_sheet_name]
new_sheet.range('A1').value = merged_df  # 将DataFrame写入新的工作表的A1单元格起始位置

# 打印合并后的DataFrame
# 打印合并后的DataFrame
print(merged_df)

# ----------------------get_merged_cells_from_starting_point---------------------------------