import xlwt

# 创建一个工作簿
xl = xlwt.Workbook(encoding='utf-8')
# 创建一个sheet对象,第二个参数是指单元格是否允许重设置，默认为False
sheet = xl.add_sheet('菜鸟的成长历程', cell_overwrite_ok=False)
# 初始化样式
style = xlwt.XFStyle()
# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
# 黑体
font.bold = True
# 下划线
font.underline = False
# 斜体字
font.italic = True
# 设定样式
style.font = font
# 第一个参数代表行，第二个参数是列，第三个参数是内容，第四个参数是格式
sheet.write(0, 0, '不带样式的携入')
sheet.write(1, 0, '带样式的写入', style)

# 保存文件
xl.save('字体.xls')