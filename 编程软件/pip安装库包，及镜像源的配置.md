# pip安装库包，及镜像源的配置



[<img src="https://devpress.csdnimg.cn/489fad64a62648818eaaebc28e5c8659.jpg" alt="img" style="zoom: 25%;" />华为云开发者联盟该内容已被华为云开发者联盟社区收录](javascript:;)

## 1 ：[pip安装](https://so.csdn.net/so/search?q=pip安装&spm=1001.2101.3001.7020)库包

1、一般pip安装库包，直接用下面命令即可：

```python
pip install package_name
```

2、指定安装库包的版本

```python
pip instal package_name==x.x.x
```

3、使用镜像源提高下载的速度（这里用[清华镜像源](https://so.csdn.net/so/search?q=清华镜像源&spm=1001.2101.3001.7020)）

```python
pip intall package_name -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 2：常用镜像源

先分享一些比较好的镜像源

```python
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/
```

## 3：三种镜像源配置方法

### （1）手动添加镜像源

使用方法：

```python
pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple
```

比如我要下载numpy这个模块，执行以下命令：

```python
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

几秒就好了：

这个方法的好处就是，你不用像其它配置一样要去配置一遍，你只需要在后面加上：

```python
-i https://pypi.tuna.tsinghua.edu.cn/simple
```

### （2）永久配置镜像源

####  方法一：到cmd执行如下命令创建pip.ini

```python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

返回：

![img](https://img-blog.csdnimg.cn/34420b433b57492e9b37c1e3678ef626.png) 

然后我们把这个路径添加到系统环境变量就好了（怎么添加环境变量？跟前面给pip添加环境变量一样操作，只是路径不一样）

####  方法二：


如果刚刚这个命令你执行失败，你可以自己在c盘创建一个文件名叫做pip，pip文件夹下创建一个文件名pip.ini,内容为

```python
[global]



index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

还是一样添加到环境变量。

### （3）pycharm内部配置

第一步：

![img](https://img-blog.csdnimg.cn/ce6ed09bc93b4b88a59e34876304c36c.png)

 第二步：

![img](https://img-blog.csdnimg.cn/2e646a4352cf47c9912ca29034d11522.png)

 第三步：

<img src="https://img-blog.csdnimg.cn/61f1224e55144f5f874989890cf334d3.png" alt="img" style="zoom:67%;" />

 <img src="https://img-blog.csdnimg.cn/1df0d50d87604fe4a025db000244f2af.png" alt="img" style="zoom:67%;" />

 第四步：
复制上面的推荐的镜像源粘贴，这里以清华镜像源为例：

<img src="https://img-blog.csdnimg.cn/245b81dd30164884929867fcc93794c2.png" alt="img" style="zoom:50%;" />

设置完后，可进行测试

 ![img](https://img-blog.csdnimg.cn/04340c3b48194ac493f7b8e4f00f484d.png)

 可快速下载就是ok了。

#### 问题,新版本的pycharm，按上面的步骤找不到**manage repositories**

<img src="https://img-blog.csdnimg.cn/27dff97066094d3f917b55f2de60c34c.png" alt="img" style="zoom:50%;" />

 