import xlwt

xl = xlwt.Workbook(encoding="utf-8")  #床i教案workbook对象
sheet = xl.add_sheet('sheet1')    #创建工作表
sheet.write(0,0,'hello')                #写入数据，第一个参数"行"，第二个参数"列"，第三个参数"内容"
xl.save('student.xls')#保存数据表

# import xlwt
#
# # 创建一个工作簿
# xl = xlwt.Workbook(encoding='utf-8')
# sheet = xl.add_sheet('菜鸟的成长历程', cell_overwrite_ok=False)
#
# # 第一个参数代表行，第二个参数是列，第三个参数是内容，第四个参数是格式
# sheet.write(0, 0, '不带样式的携入')
#
# # 保存文件
# xl.save('字体.xls')