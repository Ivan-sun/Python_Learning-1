import numpy as np

a= [1,2,3,4]
b=np.array([1,2,3,4])
''''
print('a:',a)
print('b:',b)
print('a:',type(a))
print('b:',type(b))

print('a1:',a[1])
print('b1:',b[1])
print('a[0:2]',a[0:2])
print('b[0:2]',b[0:2])

c=a*2
d=b*2

print('c:',c)
print('d:',d)
'''
# 数组的创建
a=np.array([1,2,3,4])              #一维数组
b=np.array([[1,2],[3,4],[5,6]])    #二维数组
c=np.random.randn(3)               #创建一个一维数组，服从正态分布（均值为0，标准差为1）的3个随机数
' print(c)'
d=np.arange(12).reshape(3,4)      #将一个0~11的一维数组转换成为3行4列的二维数组
print(d)
e=np.random.randint(0,10,(4,4))
print(e)