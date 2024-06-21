

'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象，所有对象可l以归纳为4种:
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
import re

from bs4 import BeautifulSoup

file=open("./baidu.html","rb")
html =file.read()
bs=BeautifulSoup(html,"html.parser")


#0.test-------------------
print(bs.title)
print(bs.a)
print(type(bs.head))

#1.Tag 标签及其内容；拿到它所找到的第一个内容
print(bs.title.string)
print(type(bs.title.string))

#2.NavigableString 标签里的内容

print(bs.a.attrs)

#3.BeautifulSoup 表示整个文档
print(type(bs))
print("文件名",bs.name)
print("标签",bs.attrs)
print(bs.a.string)

#4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号


print("*"*20)
#----------------------------------------------

#文档的遍历
#print(bs.head.contents)
print(bs.head.contents[1])


#文档的搜索


#(1)find_all()
#字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
print(t_list)
print("*"*20)
#-------------
#正则表达式搜索：使用search（）方法来匹配内容

import re
#t_list = bs.find_all(re.compile("a"))#显示所有包含a字样的内容
#print(t_list)
print("*"*20)

#方法：传入一个函数（方法），根据函数的要求来搜索

# def name_is_exits(tag):
#     return tag.has_attr("name")#搜索含有name的标签
#
# t_list = bs.find_all(name_is_exits)
# for item in t_list:
#     print(item)


#-----------------------

#2.kwargs 参数

# t_list=bs.find_all(id="head")#输出id=head 内的所有内容
# for item in t_list:
#     print(item)

t_list = bs.find_all(text=["地图","百度","贴吧"])
t_list = bs.find_all(text=re.compile("\d"))  #应用正则表达式来查找包含特定文本的内容（标签里的字符串）



#4.limit参数
t_list = bs.find_all("a",limit=2)
for item in t_list:
    print(item)


#css选择器
print(bs.select('title'))   #通过标签来查找
print(bs.select('.mnav'))   #通过类名来查找
#也能通过id、属性、子标签 来查找

