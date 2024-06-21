import os

path=os.getcwd()
print(path)

''''
如果要查看某个文件夹包含的所有文件及子文件夹的名称，可以使用os模块中的listdir()函数
'''

path='D:\\PythonLearning'
file_list=os.listdir(path)
print(file_list)

'''
如果要分离一个文件的文件主名和扩展名，可以使用splitext()函数
'''
path='example.xlsx'
separate=os.path.splitext(path)
print(separate)

'''
OS 模块中的rename（）函数可以实现重命名文件和文件夹，该函数的语法格式如下：
rename(src,dst)
'''
oldname='C:\\Users\\sun.zengchang\\Desktop\\学习\\手提包.xlsx'
newname='C:\\Users\\sun.zengchang\\Desktop\\学习\\.vscode\\手提包.xlsx'
os.rename(oldname,newname)

''''
绝对路径：表示文件的路径总是从根文件夹开始。 'd:\\example.xlsx'
相对路径：表示相对于当前运行代码文件的路径。 '.\example.xlsx'
'''

