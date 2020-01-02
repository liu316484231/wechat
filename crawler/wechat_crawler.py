# -*- coding: utf-8 -*-
import configparser
import random
import requests
import time
import pymysql

from bs4 import BeautifulSoup

from crawler.download_pic import download_pic
from crawler.html_beautify import beautify

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"

config = configparser.ConfigParser()
config.read('config.ini')

conn = pymysql.connect(config['mysql']['mysql_url'], user=config['mysql']['mysql_user'],
                       passwd=config['mysql']['mysql_password'], db=config['mysql']['mysql_db'])
cur = conn.cursor()
ggh_name = config['ggh']['ggh_name']
ggh_class = config['ggh']['ggh_class']
ggh_id = config['ggh']['ggh_id']
cookies = config['ggh']['ggh_cookies']
token = config['ggh']['ggh_token']

data = {
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": ggh_id,
    "type": "9",
}

for i in range(0, 20):
    print("第" + str(i) + "页(每页5篇文章)")
    data["begin"] = i * 5
    headers = {
        "Cookie": cookies,
        "User-Agent": ua
    }
    time.sleep(random.randint(2, 5))
    response = requests.get(url, headers=headers, params=data)
    content_json = response.json()
    print(response.text)
    print("article count:" + str(len(content_json["app_msg_list"])))
    if len(content_json["app_msg_list"]) == 0:
        break
    for item in content_json["app_msg_list"]:
        title = item['title']
        cover = item['cover']
        digest = item['digest']
        link = item['link']
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "upgrade-insecure-requests": "1"
        }
        time.sleep(random.randint(5, 10))
        # print(link)
        try:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            tag = soup.find(id="js_content")
            text = tag.text
            html = str(tag)
            item['text'] = text
            item['html'] = html
            result = (link, title, cover, digest, text, html, ggh_name,ggh_class)
            new_cover = download_pic(cover)
            new_html = beautify(html)
            sql = "insert into ggh(url,title,new_cover,digest,text,new_html,ggh_name,class) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            insert = cur.execute(sql, result)
            conn.commit()
            print('inserted ', result)
        except Exception as e:
            print(e)

cur.close()
conn.close()
