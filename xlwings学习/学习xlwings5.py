import xlwings as xw
wk = xw.Book('“轮值质量员”自查明细.xlsx')
# wk.sheets[0].copy()  # 在工作薄中复制一个工作表
# wk.sheets[0].api.Copy() # 将工作表复制，单独建立一个单独的工作簿

for sht in wk.sheets:
	wb = sht.api.Copy()
	new_workbook = xw.books[xw.books.count-1]
	new_workbook.save (r'.\拆分文件/'+sht.name+'.xlsx')
	new_workbook.close()

wk.close()

