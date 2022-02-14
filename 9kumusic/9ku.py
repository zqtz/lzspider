import requests
import re
import time
import json
from lxml import etree
from urllib import request
import os
import random
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

queue_list = Queue()
def get_url():
    for page in range(1,101):
        url = f"https://www.9ku.com/geshou/all-all-all/{page}.htm"
        queue_list.put()


def get_ids(url):
    ids = []
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.9ku.com/music/t_singer.htm",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6"
    }
    cookies = {
        "tt": "ok",
        "cc": "ok",
        "pp": "ok",
        "tmp_addplay": "",
        "Hm_lvt_2698d85c1eaff072c02e1fb3b945eaff": "1641867866,1642946551",
        "ff": "ok",
        "Hm_lvt_a5de315acb973b8e6da83458c9e456d3": "1644805106",
        "_gid": "GA1.2.374620302.1644805107",
        "Hm_lpvt_a5de315acb973b8e6da83458c9e456d3": "1644805137",
        "shows": "ok",
        "_ga": "GA1.2.86074470.1644805107",
        "_ga_4BBS961T5P": "GS1.1.1644805106.1.1.1644805216.0"
    }
    res = requests.get(url,
        headers=headers,
        cookies=cookies
    )
    pat = re.compile('blank" href="/geshou/(.*?)\.h',re.S)
    results = re.findall(pat,res.text)
    for result in results:
        ids.append(result)
    return ids

def down_music(id):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    # geshou_name = []
    songID = []  # 列表存放歌曲编号
    songName = []  # 列表存放歌曲名字
    songID1 = []  # 列表存放歌曲编号
    # 构造url
    for i in range(0, 1):
        url = f"http://www.9ku.com/geshou/{id}.htm"
        req = request.Request(url, headers=header)
        data_html = request.urlopen(req).read().decode()

        html = etree.HTML(data_html)
        pat1 = '//div[@class="singerMusic clearfix"]//div[@class="songName"]/a/@href'
        pat2 = '//div[@class="singerMusic clearfix"]//div[@class="songName"]/a//text()'

        idlist = html.xpath(pat1)
        titlelist = html.xpath(pat2)
        # 从网页中获取所有歌曲名字

        songID1.extend(idlist)  # 把多个列表合成一个列表
        songName.extend(titlelist)
        pat4 = '/play/(.*?).htm'
        for j in range(0, len(songID1)):
            idlist2 = re.findall(pat4, songID1[j])  # 从网页中获取所有歌曲ID
            songID.extend(idlist2)

    print(songName)
    print(songID)
    print(len(songName))
    print(len(songID))

    # http://www.9ku.com/html/playjs/894/893142.js
    # http://www.9ku.com/html/playjs/878/877683.js

    for i in range(0, len(songID)):
        try:
            # songurl="http://mp32.9ku.com/upload/2016/03/22/62878.m4a"   #构造歌曲url
            # songurl="http://mp3.9ku.com/hot/2004/07-13/12697.mp3"
            num = int(songID[i][0:3]) + 1
            songurl = "http://www.9ku.com/html/playjs/" + str(num) + "/" + str(songID[i]) + ".js"
            songname = songName[i]

            data2 = requests.get(songurl).text  # 在这里插入代码片
            # print(data2)

            pat3 = '"wma":"(.*?)","m4a"'
            url2 = re.findall(pat3, data2)  # 从网页中获取所有歌曲ID
            url3 = url2[0]
            result_url = eval(repr(url3).replace('\\', ''))
            print(result_url)
            data = requests.get(result_url).content
            print("正在下载第", i + 1, "首")
            url = f"http://www.9ku.com/geshou/{id}.htm"
            req = requests.get(url, headers=header)
            geshou_name = re.findall(r'<h1>(.*?)</h1>', req.text)[0]
            file_name = f'./music/{geshou_name}'
            if not os.path.exists(file_name):
                os.makedirs(file_name)
            with open(file_name + f'/{songname}.mp3', 'wb')as f:
                f.write(data)
            time.sleep(0.7)
        except ConnectionError as e:
            print(e)
            continue


# get_geshou_id()
# exit()
def main():
    ids = get_geshou_id()
    for id in ids:
        down_music(id)

if __name__ == '__main__':
    main()



