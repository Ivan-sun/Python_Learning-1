# [打不开GitHub网站100%解决办法](https://www.cnblogs.com/clark1990/p/16492296.html)

访问github.com经常打不开，无法访问。

解决Github打不开办法

打开网站http://tool.chinaz.com/dns/ ，在A类型的查询中输入 github.com，找到最快访问的ip地址，并复制下来

修改系统文件的host

##### 在hosts文件中添加：

 

```css
# localhost name resolution is handled within DNS itself.# 127.0.0.1 localhost# ::1 localhost20.205.243.166 github.com
```

 

##### 补充知识：如何修改hosts文件？

 

```css
1、右键点击hosts文件,选择复制,然后粘贴到桌面上。2、右键点击桌面上的hosts文件,选择“用记事本打开该文件”,修改之后点击【文件】>【保存】完成修改。3、将修改好的hosts文件,重新复制到 C:\Windows\System32\drivers\etc ,覆盖原来的hosts文件。
```

 

#### 3.在 CMD 命令行中执行下面语句 来刷新 DNS，重启浏览器之后就能进入Github 网址。

 

```css
 ipconfig/flushdns
```

 

 

补充：终极方法

 

记住三个网站：

github网址查询：https://ipaddress.com/website/github.com

github域名查询：https://ipaddress.com/website/github.global.ssl.fastly.net

github静态资源ip：https://ipaddress.com/website/assets-cdn.github.com

 1、打开hosts文件（C:\Windows\System32\drivers\etc）

 2、然末尾放入一下两个 IP 地址：

\# GitHub Start
140.82.114.4 github.com
199.232.69.194 github.global.ssl.fastly.net
\# GitHub End

 

保存退出

3、在 CMD 命令行中执行下面语句 来刷新 DNS，重启浏览器之后就能进入Github 网址。

ipconfig/flushdns
然后直接访问  

公司git

1、公司git需要使用代理，使用下面方式配置代理即可
git config --global http.sslverify false //不进行ssl检查，因为公司上外网是通过代理，ssl是代理发的，不是github发的，git不认。
git config --global http.proxy "http://username:password@proxycn2.huawei.com:8080/" //如果proxycn2不成功，试试proxyhk
git config --global https.proxy "https://username:password@proxycn2.huawei.com:8080/"
git config --global credential.helper store
git config --global push.default matching
git config --global http.postBuffer 2M

2、查看配置成功
git config --global --list