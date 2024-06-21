import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xlwings as xw

# 获取文件地址
file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel Files", "*.xlsx;*.xls")])
# 使用xlwings打开选择的Excel文件
wb = xw.Book(file_path)
# --------------OPEN-----------------------------
def select_and_open_excel():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 弹出文件选择对话框并获取用户选择的文件路径
    # file_path = filedialog.askopenfilename(title="选择Excel文件", filetypes=[("Excel Files", "*.xlsx;*.xls")])
    
    if file_path:  # 如果用户选择了文件
        # 使用xlwings打开选择的Excel文件
        # wb = xw.Book(file_path)
        print(f"已成功打开文件：{file_path}")
    
    root.destroy()  # 关闭Tkinter窗口

# 调用函数
select_and_open_excel()

sht1 = wb.sheets('Sheet1')
header1_range = 'A6:S6'  # Dataframe1的标题区域

header2_range = 'Z9:AJ9'  # Dataframe2的标题区域
# -----------get data----------------------------------
def get_data_from_range(sheet, header_range, start_col_num, end_col_num):
    # 将列数转换为列字母
    start_col = xw.utils.col_name(start_col_num)
    end_col = xw.utils.col_name(end_col_num)

    # 获取标题，合并单元格中的值会被展开为重复值
    headers = sheet.range(header_range).value
    # headers = [item for sublist in headers for item in sublist if item is not None]  # 将多行标题展平并去除None值

    # 确定数据范围，从第十行开始扩展到最后的非空单元格
    start_row = 10
    last_row = sheet.cells.last_cell.row
    end_row = sheet.range(f'{end_col}{last_row}').end('up').row
    data_range = sheet.range(f'{start_col}{start_row}:{end_col}{end_row}')
    
    # 读取数据
    data = data_range.value
    
    # 转换为DataFrame
    df = pd.DataFrame(data, columns=headers[:len(data[0])])  # 根据实际读取的列数确定列数
    
    # 清除空行
    df = df.dropna(how='all')  # 删除所有列都为空的行
    
    return df

# 读取Dataframe1区域的数据，A列对应第1列，S列对应第19列
df1 = get_data_from_range(sht1, header1_range, 1, 19)

# 读取Dataframe2区域的数据，Z列对应第26列，AJ列对应第36列
df2 = get_data_from_range(sht1, header2_range, 26, 36)
# print(df2)
# 以 A 列的值作为键名进行合并
merged_df = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)], axis=1)





# 将merged_df数据存储到新的工作表"1车"中
new_sheet_name = "1车"



if new_sheet_name in [sheet.name for sheet in wb.sheets]:
    wb.sheets[new_sheet_name].delete()
wb.sheets.add(new_sheet_name)  # 添加新的工作表
new_sheet = wb.sheets[new_sheet_name]
new_sheet.range('A1').value = merged_df  # 将DataFrame写入新的工作表的A1单元格起始位置

# 打印合并后的DataFrame
print(merged_df)

# ----------------------get_merged_cells_from_starting_point---------------------------------

