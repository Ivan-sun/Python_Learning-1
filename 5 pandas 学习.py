import pandas as pd
s=pd.Series(['丁一','王二','张三'])
#print(s)

#通过列表创建DataFrame
a=pd.DataFrame([[1,2],[3,4],[5,6]])
print(a)

a=pd.DataFrame([[1,2],[3,4],[5,6]],columns=['date','score'],index=['A','B','C'])
print(a)

#通过字典创建DataFrame

b=pd.DataFrame({'a':[1,3,5],'b':[2,4,6]},index=['x','y','z'])  #默认以字典的键名作为列索引
print(b)

c=pd.DataFrame.from_dict({'a':[1,3,5],'b':[2,4,6]},orient='index') #使用from_dict()函数将字典转换成DataFrame时，orient的值设为'index'，可以将字典的键名作为行索引
print(c)

#通过二维数组创建DataFrame
import pandas as pd
import numpy as np

a= np.arange(12).reshape(3,4)
b=pd.DataFrame(a,index=[1,2,3],columns=['A','B','C','D'])
print(b)

#DataFrame 的索引修改  通过index.name的属性值修改

a=pd.DataFrame([[1,2],[3,4],[5,6]],columns=['date','score'],index=['A','B','C'])
a.index.name='公司'
print(a)

#重命名索引，可以使用rename（）函数

b=a.rename(index={'A':'万科','B':'阿里','C':'百度'},columns={'date':'日期','score':'分数'})  # rename()函数不会改变a的内容，需要将其赋值给b

print('b:',b)

a.rename(index={'A':'万科','B':'阿里','C':'百度'},columns={'date':'日期','score':'分数'},inplace=True)  # 通过inplace参数一步到位的完成索引的重命名
print('a:',a)

#将行索引转化为常规列，使用reset_index()函数重置索引，同样需要将结果重新赋值给a，或者使用inplace参数设置为TRUE

a=a.reset_index()
print(a)

#将常规列转化为行索引

a=a.set_index('日期')
print(a)

#文件的读取
f= r'.\手提包.xlsx'
data=pd.read_excel(f,engine="openpyxl")
print(data)

#文件写入
data.to_excel('data.xlsx',index=False)
