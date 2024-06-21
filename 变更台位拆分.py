# -*- coding: utf-8 -*-
import xlwings as xw
xlapp = xw.App(visible= False,add_book = False)
note ="""
    ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
                                    使用前注意事项
    0.本程序支持对Office Excel的变更处理,将变更汇总表按工位进行拆分.WPS未进行测试
    1.打开的工作薄中工作表需要按照规定格式进行整理,否则数据无效！
    2.工作簿中尽量只有一个变更汇总表，其他无用工作表尽量删除！
    3.如果工作表中有与新建工作表重复的时候会报错!
    4.针对一个工作簿只能执行一次程序.如果进行第二次执行,需要将之前的工作表全部删除
    5.如果需要继续,输入总变更工作表的名称(Sheet 工作表)
    ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄  
    """
print (note)
ss = input("====确认后，按任意键加回车继续====\n")
a = xlapp.api.GetOpenFilename('Excel Files(*.xl*),*xl*',0,0,0,False)
wk = xw.Book(a)
def getsheetName(ws):
	tlist = []
	for s in ws:
		tlist.append(s.name)
	return tlist
    
while True:
    list_name = input("输入总工作表名称！输错将无效！")
    try: 
        sum_list = wk.sheets[list_name]
        break
    except:
        a = getsheetName(wk.sheets)      
        print('{0}的工作表没有"{1}"工作表！请从{2}中选择!,请重新输入'.format(wk.name,list_name,a))
        continue    

# print (sum_list.name)
s_list =[]
for cells in sum_list.range('D3:D'+str(sum_list.used_range.rows.count)):
    cells_lst=cells.value.split('、')
    for i in cells_lst:
        s_list.append(i)
# print (s_list)
s_dic= set(s_list)
# print (s_dic)
# title = sum_list.range('A2:L2').value
# print(title)
n=1
for j in s_dic:
    # print(type(j),j)
    sht = wk.sheets.add(after = wk.sheets.count)
    sht.name = str(j+'台位变更清单')
    sht.range('A1:L1').value = sum_list.range('A2:L2').value
    t = round(n/len(s_dic)*100)
    n +=1
    print('正在处理'+j+'台位中。。。',str(t)+'%' )
    i=2
    for cells in sum_list.range('D3:D'+str(sum_list.used_range.rows.count)):
        if j in cells.value:
            r=cells.row
            sht.range('A'+ str(i)+':L'+str(i)).value=sum_list.range('A'+str(r)+':L'+str(r)).value
            i +=1
print('已处理完成！')
wk.save()
wk.close()
xlapp.quit()






