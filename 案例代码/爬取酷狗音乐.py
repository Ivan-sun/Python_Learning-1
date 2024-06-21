import requests
import re

headers= {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
wangye = 'https://www.kugou.com/yy/rank/home/1-52144.html?from=homepage'


yuama = requests.get(wangye,headers=headers).text

r1 = re.findall('data-eid="(.*?)>',yuama)
print(r1)