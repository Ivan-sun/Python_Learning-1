
''''
import xlwings as xw
app= xw.App(visible= True,add_book=False)
workbook=app.books.open(r'.\“轮值质量员”自查明细.xlsx')  #打开工作簿，文件必须真实存在，且不能处于打开状态

worksheet= workbook.sheets['APM']
worksheet.range('A1').value='序号'
worksheet=workbook.sheets.add('产品统计表')
'''

# 新建一个“北京.xlsx” 工作簿，有一个名为“产品统计表的”工作表
import xlwings as xw
app= xw.App(visible=False)
workbook=app.books.add()
worksheet=workbook.sheets.add('产品统计表')
worksheet.range('A1').value='编号'
workbook.save(r'.\北京.xlsx')
workbook.close()
app.quit