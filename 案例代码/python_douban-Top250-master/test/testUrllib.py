import urllib.request

#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页源码进行utf-解码

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode('utf-8'))


#超时处理

# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

# response=urllib.request.urlopen("http://www.baidu.com")
# #print(response.status)
# print(response.getheaders())
# print("")
# print(response.getheader("Server"))



# import urllib.parse
# #Url="https://www.douban.com"
# Url="http://httpbin.org/post"
# headers={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
# }
# data=bytes(urllib.parse.urlencode({"name":"yxy"}),encoding = "utf-8")
# req = urllib.request.Request(url=Url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


#模拟浏览器访问
import urllib.parse
Url="https://www.douban.com"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
}
req = urllib.request.Request(url=Url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))