import xlwings as xw
wk = xw.Book(r'.\表格\多工作表数据汇总.xlsx')

arr = []
for sht in wk.sheets:
	if sht.name !='汇总':
		brr = []
		brr = sht.range('a2').expand().value
		arr += brr
	

#print(arr)
wk.sheets['汇总'].range('a2').value = arr