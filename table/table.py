# 使用在工作表中调用Python 自定义函数

'''
1、EXCLE 中开发工具 启用宏
2、找到xlwings模块中的xlwings.xlam 宏文件 （在Python安装路径下的site-packages文件夹）
3、开发工具中-->Excel加载项-->浏览-->找到xlwings.xlam 宏文件 进行加载
4、返回工作簿页面，在功能区可以看到xlwings选项卡。
5、根据需要找到制定的文件夹内输入cmd，-->可以使用cd命令找到对应的文件夹-->输入 xlwings quickstart table命令-->在该文件夹下将产生一个table 的文件夹包含py和xlam两个文件（table 可根据自己需要进行更换）
6、打开py文件，会自动产生模板代码，根据需要进行自定义函数
7、@xw.sub 表示这个函数只能在VBA中进行调用
8、@xw.func 表示这个函数只能通过Excel的xlwings插件导入和调用
9、 if __name__ == "__main__": 指当py 文件被直接运行时，下方的代码才会运行；当py文件以模块形式被导入时，下方的代码不会运行
10、在xlwings 选项卡内自定义代码： 
        在PYTHONPATH文本框中输入要导入的Python 自定义函数所在的文件夹位置(F:\table)
        在UDFs组件中的“UFD Modules”文本框中输入自定义函数文件的名称（table)

'''


import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("table.xlsm").set_mock_caller()
    main()
