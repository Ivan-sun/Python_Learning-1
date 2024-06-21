
'''

def input_passwd():
    # 1.提示用户输入密码
    pwd = input('请输入密码：')
    # 2.判断密码的长度
    if len(pwd) >=8:
        return pwd
    # 3.如果<8就主动抛出异常
    print('主动抛出异常')
    #a.创建异常对象
    ex = Exception('密码长度不够')
    #b.主动抛出
    raise ex
# 注意：只抛出异常而不捕获异常 代码会出错
try:
    print(input_passwd())
except Exception as re:
    print(re)

'''

def demo1():
    return int(input('请输入整数:'))

def demo2():
    return demo1()

# 函数的错误：一级一级的去找，最终会将异常传递到主函数里
try:
      print(demo2())
except Exception as r:
    print('未知错误 %s' %r)
print(demo2())
