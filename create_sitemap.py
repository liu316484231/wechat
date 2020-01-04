import datetime
import os
import re

from db import DB


def creat_xml(filename, url_list):  # 生成sitemap所需要的xml方法
    if os.path.exists(filename):
        os.remove(filename)
    header = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(header)
    file.close()

    for url in url_list:
        times = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        urls = re.sub(r"&", "&amp;", url)  # 注意这里,在URL中如果含有&将会出错,所以需要进行转义

        # 这个是生成的主体,可根据需求进行修改
        ment = "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n" % (
        urls, times)

        file = open(filename, 'a', encoding='utf-8')
        file.writelines(ment)
        file.close()

    last = "</urlset>"
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(last)
    file.close()


if __name__ == '__main__':
    host = "https://www.bing.com"
    with DB() as db:
        db.execute('select id,class from ggh')
        result = db.fetchall()
        url_list = []
        for item in result:
            id = item['id']
            cls = item['class']
            url_list.append(host + "/" + cls + "/" + str(id))

    creat_xml("./static/sitemap.xml", url_list)
