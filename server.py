import asyncio
from flask import Flask, jsonify, request
from flask import render_template

from model import get_article, get_list, get_count, get_list_rand
from thread import MyThread
from util.chinese_translate import chs_to_cht
from util.util import process_data_index

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'health': 'ok'})


@app.route('/', methods=['GET'])
def index():

    # rec = get_list_rand(0, 6, "all")
    # top = get_list_rand(0, 6, "all")
    # food = get_list(0, 5, "food")
    # movie = get_list(0, 5, "movie")
    # yingxiao = get_list(0, 5, "yingxiao")
    # 以下改為多線程去拉
    t1 = MyThread(get_list_rand, (0,6,"all"))
    t2 = MyThread(get_list, (0,6,"all"))
    t3 = MyThread(get_list, (0,5,"food"))
    t4 = MyThread(get_list, (0,5,"movie"))
    t5 = MyThread(get_list, (0,5,"net"))
    t_list = [t1, t2, t3, t4, t5]
    for t in t_list:
        t.start()
        t.join()
    rec = t1.get_result()
    top = t2.get_result()
    food = t3.get_result()
    movie = t4.get_result()
    net = t5.get_result()
    data = {
        'rec': process_data_index(rec),
        'top':  process_data_index(top),
        'food':  process_data_index(food),
        'movie':  process_data_index(movie),
        'net':  process_data_index(net),
    }
    return render_template('index.html', data=data)


@app.route('/<string:cls>/<int:id>', methods=['GET'])
def article(cls, id):
    result = get_article(cls, id)
    if result == None:
        return render_template('404.html')
    rec = get_list_rand(0, 6, "all")
    list_rec = []
    for item in rec:
        list_rec.append({
            'id': item['id'],
            'title': chs_to_cht(item['title'])[:20],
            'class': item['class'],
            'digest': chs_to_cht(item['digest'])[:20] + "...",
            'cover': item['cover']
        })
    data = {
        'title': chs_to_cht(result['title']),
        'html': chs_to_cht(result['html']),
        'digest' : chs_to_cht(result['digest']),
        'list' : list_rec
    }
    return render_template('article.html', data=data)


@app.route('/list/<string:cls>/', methods=['GET'])
def list(cls):
    num = int(request.args.get("num"))
    count = int(request.args.get("count"))
    if count > 20:
        return render_template('404.html')
    result = get_list(num, count, cls)
    list = []
    sum = get_count(cls)
    for item in result:
        list.append({
            'id': item['id'],
            'title': chs_to_cht(item['title']),
            'class': item['class'],
            'digest': chs_to_cht(item['digest']),
            'cover': item['cover']
        })
    all_page_name = int(sum / count) + 1
    if all_page_name > 20:
        all_page_name = 20
    data = {
        'list': list,
        'count': all_page_name,
        'cls': cls,
        'pageNum': num,
    }

    return render_template('list.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

