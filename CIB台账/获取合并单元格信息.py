

import xlwings as xw
import pandas as pd

# 打开 Excel 文件
file_path = '.\CIB台账\巴西圣保罗项目单轨项目.xlsx'
wb = xw.Book(file_path)
sht1 = wb.sheets[0]

# 定义将列字母转换为列索引的函数
def col2num(col):
    num = 0
    for c in col:
        num = num * 26 + ord(c.upper()) - ord('A') + 1
    return num

# 定义将列索引转换为列字母的函数
def column_index_to_letter(column_index):
    letter = ''
    while column_index > 0:
        column_index, remainder = divmod(column_index - 1, 26)
        letter = chr(65 + remainder) + letter
    return letter

# 定义获取合并单元格信息的函数
def get_merged_cells_from_starting_point(sht1, start_col_letter, start_row):
    merged_cells_info = []
    start_col_index = col2num(start_col_letter)

    # 获取所有合并单元格区域
    for cell in sht1.api.UsedRange:
        if cell.MergeCells:
            cell_range = cell.MergeArea
            start_cell = (cell_range.Row, cell_range.Column)
            end_cell = (cell_range.Row + cell_range.Rows.Count - 1, cell_range.Column + cell_range.Columns.Count - 1)
            if start_cell[0] == start_row and start_cell[1] >= start_col_index:
                cell_length = cell_range.Columns.Count
                cell_content = sht1.range(start_cell[0], start_cell[1]).value
                merged_cells_info.append({
                    'start_cell': f"{column_index_to_letter(start_cell[1])}{start_cell[0]}",
                    'end_cell': f"{column_index_to_letter(end_cell[1])}{end_cell[0]}",
                    'length': cell_length,
                    'content': cell_content
                })

    return merged_cells_info

# 获取从 Z 列第八行开始的合并单元格信息
specific_merged_cells_info = get_merged_cells_from_starting_point(sht1, 'Z', 8)

# 将结果转换为 DataFrame
df = pd.DataFrame(specific_merged_cells_info)

# 在新的工作表中存储结果
sht2 = wb.sheets.add('sht2')
sht2.range('A1').value = df

# 保存并关闭工作簿
wb.save('你的保存路径.xlsx')
wb.close()
