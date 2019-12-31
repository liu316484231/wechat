from db import DB


def get_article(cls,id):
    with DB() as db:
        db.execute('select * from ggh where id=%s and class=%s', (id,cls))
        result = db.fetchone()
        print(result)
        return result

# 从0开始
def get_list(pageNum, pageCount, cls="all"):
    start = pageNum * pageCount
    offset = pageCount
    with DB() as db:
        if cls == "all":
            db.execute('select id,title,cover,digest,class from ggh ORDER BY RAND() limit %s, %s', (start, offset))
        else:
            db.execute('select id,title,cover,digest,class from ggh where class=%s ORDER BY RAND() limit %s, %s', (cls, start, offset))
        result = db.fetchall()
        print(result)
        return result

def get_count(cls="all"):
    with DB() as db:
        if cls == "all":
            db.execute('select count(*) as count from ggh')
        else:
            db.execute('select count(*) as count from ggh where class=%s', (cls))
        result = db.fetchone()
        print(result)
        return int(result['count'])

if __name__ == '__main__':
    get_list(0,2)