import xlwings as xw
wk = xw.Book()

for i in range (12,0,-1):
	sht = wk.sheets.add()
	sht.name = str(i)+'月'

for sh in wk.sheets:
	if '月' in sh.name:
		sh.delete()
