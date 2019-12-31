import json
import os
import pickle
from nlp.preprocess import PreProcess
from gensim import corpora

def __set_origin_corpus(self):
    if ('dictionary.txt' in os.listdir()):
        print("----------语料库已经构建---------")
        self.dictionary = corpora.Dictionary.load_from_text('dictionary.txt')
        return
    with open('doc.json', 'r', encoding='gbk') as f:
        doc = json.load(f)
    corpus = []
    text = []
    # 引入预处理模块
    pre = PreProcess()
    for doc_item in doc:
        with open(self.dir + doc_item['name'], 'r', encoding='gbk') as f:
            text.append(f.read())
    for item in text:
        pre_doc = pre.cut(pre.clean_doc(item))
        corpus.append(pre_doc)
    dictionary = corpora.Dictionary(corpus)
    # 将字典库保存为txt
    dictionary.save_as_text('dictionary.txt')
    corp = []
    print('----------词典构建完毕，目前共有词:%d 个---------' % len(dictionary.keys()))
    for item in text:
        corp.append(dictionary.doc2bow(pre.cut(pre.clean_doc(item))))
    # 将语料库存储为pkl序列
    with open('corpus.pkl', 'wb') as f:
        pickle.dump(corp, f)
    self.corp = corp
    print('----------语料库构建完毕---------')


def update(self, new_dir):
    if os.path.exists('dictionary.txt'):
        dictionary = corpora.Dictionary.load_from_text('dictionary.txt')
    else:
        print('----------词典库还未构建---------')
        return
    new_doc_name = os.listdir(new_dir)
    with open('doc.json', 'r', encoding='gbk') as f:
        doc = json.load(f)
    num = doc[-1]['id']
    for doc_item in new_doc_name:
        num += 1
        doc_item.replace('/', '')
        doc.append({'id': num, 'name': doc_item, 'url': new_dir + doc_item})
    with open('doc.json', 'w', encoding='gbk') as f:
        f.truncate()
        json.dump(doc, f)
        print('----------文本库已更新---------')
    add_corpus = []
    add_text = []
    pre = PreProcess()
    for doc_item in new_doc_name:
        with open(new_dir + doc_item, 'r') as f:
            add_text.append(f.read())
    print('----------新增添文章:%d 篇---------' % len(new_doc_name))
    for item in add_text:
        add_pre_doc = pre.cut(pre.clean_doc(item))
        add_corpus.append(add_pre_doc)
    dictionary.add_documents(add_corpus)
    if len(dictionary.keys()) >= 10:
        os.remove('dictionary.txt')
        dictionary.save_as_text('dictionary.txt')
        print('----------字典库已更新完毕---------')
        print('----------更新后的字典库有词：%d 个---------' % len(dictionary.keys()))
    corp = []
    text = []
    for item in doc:
        try:
            with open(item['url'], 'r', encoding='gbk') as f:
                text.append(f.read())
        # 如果gbk方式不行则更换编码utf8进行读取
        except UnicodeDecodeError:
            with open(item['url'], 'r') as f:
                text.append(f.read())
            continue
    for item in text:
        corp.append(dictionary.doc2bow(pre.cut(pre.clean_doc(item))))
    with open('corpus.pkl', 'wb') as f:
        f.truncate()
        pickle.dump(corp, f)
    self.corp = corp
    print('----------语料库更新完毕---------')
