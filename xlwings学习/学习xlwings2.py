import xlwings as xw
wk = xw.Book('学生成绩表.xlsx')
sht = wk.sheets[0]
rng = sht.range('e1')
rng.value = 1
rng.value = [1,2,3]   #横向赋值
rng.value = [[1],[2],[3]]	#纵向赋值
rng.value = [[1,2,3],[4,5,6],[7,8,9]]	#区域赋值
rng.resize(3,3).clear_contents()		#清空内容    
maxrow = sht.range('a1').end('down').row #获取最大行数
maxclo = sht.used_range.columns.count 		#获取最大列数
# print (maxrow,maxclo)
#print (type(maxrow))
arr = sht.range('a1:c'+str(maxrow)).value
#print (arr)	
rng.value = arr
#------------------------------------------
brr =sht.range('a1').expand().value
print(brr)
rng.value = brr
#-----------------------------------------