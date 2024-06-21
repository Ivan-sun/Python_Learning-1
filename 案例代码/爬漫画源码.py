#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests # 数据请求模块
import parsel # 数据解析模块  用于解析json数据 融合了正则表达式提取的功能 不支持3.9版本
import os # 提供了各种python程序与操作系统进行交互的接口的一个模块

# 妖神记漫画网址
url = 'https://www.mkzhan.com/207622/'

# 请求头
headers = {
    'Cookie': '__login_his_sync=0; redirect_url=%2F207622%2F; UM_distinctid=18929cac20955b-0ed238a4d7fd63-7e56547f-1fa400-18929cac20ac70; CNZZDATA1261814609=1457200997-1688620024-%7C1688620024; CNZZDATA1262045698=972920694-1688623264-%7C1688623264; tourist_expires=1; cn_1262045698_dplus=%7B%22distinct_id%22%3A%20%2218929cac20955b-0ed238a4d7fd63-7e56547f-1fa400-18929cac20ac70%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201688623310%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201688623310%7D',
    'referer': 'https://www.mkzhan.com/category/?is_vip=1',
    'host': 'www.mkzhan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
}

# 向漫画网址发送请求
resp = requests.get(url,headers=headers)

# 解析数据，处理网页源代码
selector = parsel.Selector(resp.text)

# 通过Selector对象来选择源代码中的特定元素
li_list = selector.css('.chapter__list-box li')

# print(li_list) # 返回的列表，列表里面每一个元素都是selector对象 这个对象可以调用css的语法

# 通过for循环遍历 并且进行了排序  从第一话开始
for li in list(reversed(li_list[2:])):
    # 拿到章节id
    img_id = li.css('a::attr(data-chapterid)').get()
    # 拿到章节标题
    title = li.css('a::text').get().strip()

    if not title:
        title = li.css('a::text').getall()[1].strip()


    file_name = f'{title}\\'

    if not os.path.exists(file_name):
        os.mkdir(file_name)

    # 章节网址
    index_url = 'https://comic.mkzcdn.com/chapter/content/v1/'

    # 配置数据参数
    data = {
        'chapter_id': img_id,
        'comic_id': '207622',
        'format': '1',
        'quality': '1',
        'type': '1',
    }
    # 向每一章漫画网址发送请求，获取图片数据

    json_data = requests.get(index_url, params=data).json()
    # print(json_data)

    imgs = json_data['data']['page']
    print(imgs)
    page = 0
    # 拿到图片url地址
    for img in imgs:
        img_url = img['image']
        # 向图片网址发送请求，获取.content数据
        img_content = requests.get(img_url).content
        # 打印标题和漫画图片网址
        print(title, img_url)

        page += 1
        # 保存图片到本地文件夹
        with open(file_name+str(page)+'.jpg', 'wb')as f:
            f.write(img_content)




