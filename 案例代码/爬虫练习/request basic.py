import requests
url = 'http://www.baidu.com'
response = requests.get(url)

# print(response.text)
# print(response.content.decode())
# 响应的url
# print(response.url)
# 响应状态码
# print(response.status_code )
# 响应对应的请求头
# print(response.request.headers)
# print('------------------------------')
# 相应头
# print(response.headers)
# 答应响应设置cookies
print(response.cookies)