import xlwings as xw
'''

xlapp = xw.App(visible= True,add_book = True)
wk = xw.Book()

wb = xw.Book('“轮值质量员”自查明细.xlsx')

sht = wb.sheets.add()
sht.name = '你好'

for sh in wb.sheets:
	print (sh.name)
for i in range(0,wb.sheets.count):
	print (wb.sheets[i].name)

s = wb.sheets.add(after = wb.sheets.count)
wb.sheets['APM'].copy()
wb.sheets['APM (2)'].delete()

'''

wk = xw.Book('“轮值质量员”自查明细.xlsx')
'''
slist = []
for sht in wk.sheets:
	slist.append(sht.name)
print (slist)
'''
'''
def getsheetName(ws):
	tlist = []
	for s in ws:
		tlist.append(s.name)
	return tlist

for a in getsheetName(wk.sheets):
	print (a)
'''
# 获取单元格的值
# 使用api方式时，函数的字母需注意大小写，与VBA中的格式一致
sh = wk.sheets['APM']
print (sh.range('A1').value)
print (sh.range('E2').api.Value)
wk.sheets.api.Add()
sh.range('N1').api.Value = 'xlwings'
print (sh.range('b2').expand().value)
print (sh.range('b2').expand().rows.count)
r = sh.range('A65536').end('up').row   # 从表底向上查，找到最后一行 Ctrl + ↑ 
print(r)
r = sh.range('a1').end('down').row     # 从表底向上查，找到最后一行 Ctrl + ↓
print(r)
r = sh.range('a65536').api.End(-4162).Row  # -4162 代表VBA中的常量‘xlUp' Ctrl + ↑
print (r)
r= sh.range('a1').api.End(-4121).Row  #-4121 代表VBA中的常量‘xlDown' Ctrl + ↓
sh.range('a1').font.italic = True    # 改为斜体
print(sh.range('a1').font.name)			# 字体名称
sh.range('a1').font.api.Strikethrough = True  # Python 中没有的函数可以使用api,Strikethrough 增加删除线
