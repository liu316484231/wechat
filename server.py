from flask import Flask ,jsonify ,abort,request
import json

from flask import render_template

from crawler.download_pic import download_pic
from crawler.html_beautify import beautify
from model import get_article, get_list, get_count

app = Flask(__name__)

@app.route('/health',methods = ['GET'])
def health():
    return jsonify({'health':'ok'})

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

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
            'digest' : item['digest'],
            'class' : item['class'],
            'title' : item['title'],
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