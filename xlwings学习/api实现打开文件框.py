import xlwings as xw
xlapp = xw.App(visible=True,add_book = False)
a = xlapp.api.GetOpenFilename('Excel Files(*.xl*),*xl*',0,0,0,True)  # 将 True 改为False 只打开一个文件
print(a)


# s_list = []
# for i in a:
# 	wk = xw.Book(i)
# 	for s in wk.sheets:
# 		s_dict = {}
# 		s_dict['工作簿名字'] = wk.name
# 		s_dict['工作表名字'] = s.name
# 		s_list.append(s_dict)
# 	wk.close()
# print(s_list)

# =======列表推导式================
# t_list = []
# for i in a:
# 	wk = xw.Book(i)
# 	t_list += [{'工作簿名字':wk.name,'工作表名字':s.name} for s in wk.sheets]
# 	wk.close()
# print(t_list)