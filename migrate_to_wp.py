import configparser
import json
import datetime
import urllib.parse
import pymysql
from util.chinese_translate import cht_to_chs
from util.util import hanzi_to_pinyin

config = configparser.ConfigParser()
config.read('config.ini')

conn = pymysql.connect(config['mysql_wp']['mysql_url'],
                       user=config['mysql_wp']['mysql_user'],
                       passwd=config['mysql_wp']['mysql_password'],
                       db=config['mysql_wp']['mysql_db'],
                       port=int(config['mysql_wp']['mysql_port']),
                       )
cur = conn.cursor()

# inserted file list
# poet.tang.0.json
# lunyu
# shijing
# sishuwujing: zhongyong mengzi daxue





cate = {"class": "宋词", "id": 5}
file_path = '/Users/admin/github/chinese-poetry/json/poet.song.0.json'

with open(file_path, 'r') as fw:
    result = fw.read()
    data = json.loads(result)
    for item in data:
        author, graphs, chapter, title, section = (None, None, None, None, None)
        if "author" in item:
            author = cht_to_chs(item['author'])
        if "chapter" in item:
            chapter = cht_to_chs(item['chapter'])
        if "title" in item:
            title = cht_to_chs(item['title'])
        if "section" in item:
            section = cht_to_chs(item['section'])
        if "paragraphs" in item:
            graphs = item['paragraphs']
        print(title,chapter,section,graphs)
        # set title
        # title = chapter

        wp_content = "<!-- wp:heading --><h2>" + cate["class"] + "：" + title + "</h2><!-- /wp:heading -->"
        if author != None:
            wp_content +=  "<!-- wp:heading --><h2>作者：" + author + "</h2><!-- /wp:heading -->"

        for p in graphs:
            wp_content += "<!-- wp:paragraph --><p>" + cht_to_chs(p) + "</p><!-- /wp:paragraph -->"

        # check exist or not
        cur.execute("select * from wp2posts where post_title = %s", title)
        res = cur.fetchone()
        if res != None:
            print("数据已经存在！跳过")
            continue

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post_name = urllib.parse.quote(title[0:10])
        inserted = (1, now, now, wp_content, title, post_name, now, now, "", "", "", "")
        cur.execute(
            "insert into wp2posts(post_author,post_date,post_date_gmt,post_content,post_title,post_name,post_modified,post_modified_gmt,post_excerpt,to_ping,pinged,post_content_filtered) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            inserted)
        id = conn.insert_id()
        print("插入成功:" + str(id))

        cur.execute("insert into wp2term_relationships(object_id,term_taxonomy_id) values (%s,%s)", (id, cate["id"]))

        # 注释部分为增加作者tag 暂时不去弄了
        # author_tag = hanzi_to_pinyin(author)
        # cur.execute("select * from wp2terms where slug = %s", author_tag)
        # res = cur.fetchone()
        # print(res)
        # if res == None:
        #     cur.execute( "insert into wp2terms(name,slug) values(%s,%s)", (author, author_tag))
        #     term_id = conn.insert_id()
        #     print("插入term成功:" + str(term_id))
        #     cur.execute("insert into wp2term_taxonomy(term_id,taxonomy,description) values (%s,%s,%s)", (term_id, "post_tag",""))
        # else:
        #     term_id = res[0]
        # cur.execute("insert into wp2term_relationships(object_id,term_taxonomy_id) values (%s,%s)", (id, term_id))
        #


        conn.commit()

        # break

cur.close()
conn.close()


# <!-- wp:heading -->
# <h2>唐诗：横吹曲辞 后出塞五首 二</h2>
# <!-- /wp:heading -->
#
# <!-- wp:heading -->
# <h2>作者：杜甫</h2>
# <!-- /wp:heading -->


# <!-- wp:paragraph -->
# <p>作者：太宗皇帝</p>
# <!-- /wp:paragraph -->
#
# <!-- wp:paragraph -->
# <p>秦川雄帝宅，函谷壯皇居。</p>
# <!-- /wp:paragraph -->
#
# <!-- wp:paragraph -->
# <p>綺殿千尋起，離宮百雉餘。</p>
# <!-- /wp:paragraph -->
#
# <!-- wp:paragraph -->
# <p>連甍遙接漢，飛觀迥凌虛。</p>
# <!-- /wp:paragraph -->
#
# <!-- wp:paragraph -->
# <p>雲日隱層闕，風煙出綺疎。</p>
# <!-- /wp:paragraph -->
