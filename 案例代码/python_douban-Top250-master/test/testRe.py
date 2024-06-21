#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re

#创建模式对象

pat=re.compile("AA")#此处的AA，是正则表达式，用来去验证其他的字符串
m=pat.search("CBAACDAEAAsdaf")#search方法，进行比对查找
print(m)

#没有模式对象
m=re.search("AA","fasdgdsAA,dfdf456")#前面的字符串是规则（模板），后面的字符串是被校验的对象
print(m)


print(re.findall("[A-Z]","AfghSl.kDsadfsdfafdg"))#前面的字符串是规则（模板），后面的字符串是被校验的对象


print(re.findall("[A-Z]+","AFfghHGSl.kDsadfsdfafdg"))

print(re.sub("a","A","abcdcafd"))#找到a用A替换，在第三个字符串中查找a

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a=r"\aabd-'\'"
print(a)