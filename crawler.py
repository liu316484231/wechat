# -*- coding: utf-8 -*-
import json
import random
import requests
import time
import pymysql
from bs4 import BeautifulSoup

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

cookies = "noticeLoginFlag=1; pgv_pvi=8630118400; RK=pSDsiEPdep; ptcz=4f89a5ca5e7dc1c9c70fca78339ebac88b58f1d3a9d95e529628868c3a41d1df; pgv_pvid=6773863088; tvfe_boss_uuid=7851eabcf5c5022c; o_cookie=330899380; pac_uid=1_330899380; _ga=amp-WuQjnYbqED5FeJbpX0rqnw; ua_id=8NsNlnCN9KFUgjYVAAAAAG-1bqLLFNotQBXXETR9ehQ=; rewardsn=; wxtokenkey=777; pgv_info=ssid=s8132691250; pgv_si=s8748705792; uin=o0330899380; skey=@QL5ApJAy6; ptisp=cnc; cert=_HdeIKdqUnaE2hVQNB2VPMYp6TA2JLBt; master_key=9oyjTYM/Jfhy5xTFjFcXNSbvolW9fY8ljLXEOHGNEns=; mmad_session=106b28e70bbe5ec8a61cba41edf7962b5d4e0d852cdabd92504a924821caaf370339552f26c6baa78a9e1b3451067acf4cb1c4d6c71357b09e73dc4047fde31a44c51e15c5493f767e30f9443edad8d712f5581b1e91ef87c87dcd92f20a3c6f11de1c56c245721266e7088080fefde3; ts_uid=3915319817; mm_lang=zh_CN; sig=h01a21dc48fa215da9d8cb7889b14fbbb58af92114baa028d95ff0369a1d342b6fdc0c3f8501b094f2a; ticket_id=gh_7a72c9040749; uuid=a438ea65e0923064e3c2b914a108d507; bizuin=3231272072; ticket=03f9c38ca99ff4701af649288f1f9407f0ec52a0; data_bizuin=3231272072; data_ticket=6K6i3bpF/8HUsMb9kESaSlVaT34o/CeO/0SZgnn+w/tvIJ7q+suWVvcwEaL965Y5; slave_sid=MjZDYTIyV2dNOGpYbTRVdjFFMkZMZkdHUXpxU3NsYTdvamxiallVbEFld2xYNnd4dkNjTEl3dVZzZkp5OHVlYktZakRxZ3hWbDNUMENUN0tlcF9PYVBVa1V0R2dvc2dWS21jY0lKTHkwVFpkaVJmRGdQUmVubTVDZ2EyaVNaZ0ptWUJ5WE10Vm40Z2dEVjBi; slave_user=gh_7a72c9040749; xid=f1db1a0c587afd3a9bc13709fff6704f; openid2ticket_oiEyZwIMCgGIvj_V2iByqiLv166w=EF1OZB+u09izrdjdlUBgQkXu9D+dGjVFUTfUzKFj0xk="
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"

data = {
    "token": "881855475",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzU0OTA0MjQ0Ng==",
    "type": "9",
}

conn = pymysql.connect('*', user="*", passwd="*", db="*")
cur = conn.cursor()

ggh_name="*"

for i in range(0,100):
    print("begin:" + str(i*5))
    data["begin"] = i * 5
    headers = {
        "Cookie": cookies,
        "User-Agent": ua
    }
    time.sleep(random.randint(2,5))
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
        time.sleep(random.randint(3, 6))
        # print(link)
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        tag = soup.find(id="js_content")
        text = tag.text
        html = str(tag)
        item['text'] = text
        item['html'] = html
        result = (link, title, cover, digest, text, html,ggh_name)
        sql = "insert into ggh(url,title,cover,digest,text,html,ggh_name) values(%s,%s,%s,%s,%s,%s,%s)"
        try:
            insert = cur.execute(sql, result)
            conn.commit()
            print('inserted ', result)
        except Exception as e:
            print(e)

cur.close()
conn.close()
