from flask import Flask ,jsonify ,abort,request
import json

from flask import render_template

from crawler.download_pic import download_pic
from crawler.html_beautify import beautify
from model import get_article, get_list, get_count
from util.chinese_translate import chs_to_cht

app = Flask(__name__)

@app.route('/health',methods = ['GET'])
def health():
    return jsonify({'health':'ok'})

@app.route('/',methods = ['GET'])
def index():
    rec = get_list(0, 6, "all")
    top = get_list(0, 6, "all")
    food = get_list(0, 5, "food")
    list_rec = []
    list_top = []
    list_food = []
    for item in rec:
        list_rec.append({
            'id': item['id'],
            'title': chs_to_cht(item['title'])[:20],
            'class': item['class'],
            'digest': chs_to_cht(item['digest'])[:20]+"...",
            'cover': download_pic(item['cover'])
        })
    for item in top:
        list_top.append({
            'id': item['id'],
            'title': chs_to_cht(item['title'])[:20],
            'class': item['class'],
            'digest': chs_to_cht(item['digest'])[:20]+"...",
            'cover': download_pic(item['cover'])
        })
    for item in food:
        list_food.append({
            'id': item['id'],
            'title': chs_to_cht(item['title'])[:20],
            'class': item['class'],
            'digest': chs_to_cht(item['digest'])[:20]+"...",
            'cover': download_pic(item['cover'])
        })
    data = {
        'rec': list_rec,
        'top': list_top,
        'food' : list_food,
    }
    return render_template('index.html', data=data)

@app.route('/<string:cls>/<int:id>',methods = ['GET'])
def article(cls,id):
    result = get_article(cls,id)
    if result == None:
        return render_template('404.html')
    data = {
        'title' : result['title'],
        'html' : beautify(result['html'])
    }
    return render_template('article.html', data=data)

@app.route('/list/<string:cls>/',methods = ['GET'])
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
            'id' : item['id'],
            'title': chs_to_cht(item['title']),
            'class': item['class'],
            'digest' : chs_to_cht(item['digest']),
            'cover' : download_pic(item['cover'])
        })
    all_page_name = int(sum/count)+1
    if all_page_name > 20:
        all_page_name = 20
    data = {
        'list' : list,
        'count' : all_page_name,
        'cls' : cls,
        'pageNum' : num,
    }

    return render_template('list.html', data=data)


if __name__ == '__main__':
    app.run(debug = True)