import xlwings as xw
wk = xw.Book()
wk.sheets.add(before = 1)
wk.sheets.add(after = wk.sheets.count)
sht = wk.sheets.add(before= 1)
sht.name = '目录'
sht.range('a1').value = "目录"
slist = []
for s in wk.sheets:
	if s.name != "目录":
		slist.append([s.name])
sht.range('a2').value =slist

