from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error          #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作
#引入第三方模块

#正则表达式规则
#获取影片详情链接规则
findLink=re.compile(r'<a href="(.*?)">')       #创建正则表达式对象目标是规则（字符串模式）
#获取影片图片规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#re.S是忽略换行符
#获取影片片名
findName=re.compile(r'<span class="title">(.*?)</span>',re.S)
#获取影片评分
findScore=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#获取评价人数
findJudge =re.compile(r'<span>(.*?)</span>')
#获取概况
findInq=re.compile(r'<span class="inq">(.*?)</span>')
#获取影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)



def main():
    baseurl="https://movie.douban.com/top250?start=0"
    savepath="./豆瓣电影Top250.xls"
    #1.爬取网页并解析数据
    datalist =getData(baseurl)

    #2.保存数据
    saveData(savepath,datalist)



#得到指定一个URL的网页内容
def askURL(url):
    head={              #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是高数浏览器，我们可以接收什么水平的消息）
    request=urllib.request.Request(url=url,headers=head)
    html=""     #该网页内容源码
    try:
        response = urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
       # print(html)    #打印网页
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html




#爬取网页
def   getData(baseurl):
    dataList=[]
    for i in range(0,10):       #调用获取页面信息的函数，10次，一页25条
        url = baseurl+str(i*25)
        #print(url)
        html=askURL(url)

        # 2.逐一                                                                                                                                                                                             解析数据
        soup=BeautifulSoup(html,"html.parser")#对html解析形成树形结构
        for item in soup.find_all('div',class_="item"):     #查找符合的字符串，形成列表,class要加下划线表示属性
            print("正在获取信息......")
            #print(item)#打印测试:查看电影item全部信息
            data = []  #该列表保存一部电影全部信息
            item=str(item)
            #通过正则表达式获取内容

            #获取影片详情链接
            link=re.findall(findLink,item)[0]   #re库用来通过正则表达式查找指定的字符串，0表示只要第一个链接
            data.append(link)
            #print(link)
            #获取影片图片
            image=re.findall(findImgSrc,item)[0]
            data.append(image)
            #print(image)
            #获取影片名字
            name=re.findall(findName,item)
            if(len(name)==2):
                cname=name[0]
                data.append(cname)
                oname=name[1].replace("/","")
                data.append(oname)
            else:
                data.append(name)
                data.append(' ')  #留空
            #print(name)
            # 获取影片评分
            score=re.findall(findScore,item)[0]
            data.append(score)
            #print(score)
            # 获取评价人数
            judgenum=re.findall(findJudge,item)[0]
            data.append(judgenum)
            #print(judgenum)
            # 获取概况
            inq=re.findall(findInq,item)
            if len(inq)!=0:
                inq = inq[0].replace("。","")#去掉句号
                data.append(inq)
            else:
                 data.append(" ")    #留空
            #print(inq)

            # 获取影片的相关内容
            bd=re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/>
            bd = re.sub('/'," ",bd)
            data.append(bd.strip()) #去掉前后的空格
            #print(bd)

            dataList.append(data)
    print(dataList)
    return dataList




#保存数据
def saveData(savepath,datalist):
    print("saveing/正在保存到excel文档......")
    xl = xlwt.Workbook(encoding="utf-8")
    worksheet = xl.add_sheet('豆瓣电影Top250')
    col = ('电影详情链接',"图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0, 8):
        worksheet.write(0,i,col[i])#列明
    for i in range(0,250):
        print("正在写入第%d条"%i)
        data =datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])

    xl.save("豆瓣电影top250.xls")   #保存
    print("");
    print("写入完成！！！")


#保证单一入口
if __name__ =="__main__":       #当程序执行时
    #调用函数
    main()