import os
file_path = os.getcwd()
print('本文件地址：'+file_path+'\n'
      '----------------------------------------------------')

file_list = os.listdir()
for i in file_list:
    print(i)

print('\033[0:35m\t图书印象馆\033[')

    
'''
    考虑如何建立文件夹的目录？
      可以选择 1、仅建立一级目录；转出到Excel文件工作表中
               2、建立2级目录，并转出到Excel文件中
               3、建立所有等级的目录；


'''
