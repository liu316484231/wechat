from crawler.download_pic import download_pic
from crawler.html_beautify import beautify
from db import DB

with DB() as db:
    db.execute('select * from ggh')
    result = db.fetchall()
    print("data len :" + str(len(result)))
    while result != None:
        for item in result:
            try:
                id = item['id']
                cover = item['cover']
                html = item['html']
                if cover.startswith('http') == False:
                    continue
                new_cover = download_pic(cover)
                new_html = beautify(html)
                db.execute('update ggh set cover=%s, html=%s where id=%s',(new_cover,new_html,id))
                print("updated item:" + str(id))
            except Exception as e:
                print(e)

