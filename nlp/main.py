from gensim import corpora
from gensim import models

from gensim.corpora import dictionary



def run():
    word_list1 = ['我', '来自', '中国', '我']
    word_list2 = ['我们', '来自', '火星']
    word_list3 = ['你', '来自', '何方']

    # 利用list1和list2生成一个词典
    dict = corpora.Dictionary([word_list1, word_list2])
    print('由list1和list2生成的词典：')
    print(dict)

    dict.add_documents([word_list3])
    print('由list3拓展生成的词典：')
    print(dict)
    dict.save('test.dict')  # 保存字典
    dict = corpora.Dictionary.load('test.dict')

    print('dfs:', dict.dfs)  # 字典词频，{单词id，在多少文档中出现}
    print('num_docs:', dict.num_docs)  # 文档数目
    print('num_pos:', dict.num_pos)  # 所有词的个数（不去重）
    word_id_dict = dict.token2id  # 生成{词:id}这样一个字典
    id_word_dict = dict.id2token  # 生成{id:词}这样一个字典
    print('word_id_dict：', word_id_dict)
    print('id_word_dict：', id_word_dict)

    word_bow1 = dict.doc2bow(word_list1, allow_update=False)  # 词袋[(id,num)],稀疏向量
    word_bow2 = dict.doc2bow(word_list2)  # 将词列表转换成稀疏词袋向量
    word_bow3 = dict.doc2bow(word_list3)  # 将词列表转换成稀疏词袋向量
    print('word_bow1:', word_bow1)
    print('word_bow2:', word_bow2)
    print('word_bow3:', word_bow3)
    corpus = [word_bow1, word_bow2, word_bow3]  # 由词袋向量组成的列表构成语料
    print(corpus)

    tfidf_model = models.TfidfModel(corpus=corpus, dictionary=dict)
    print(tfidf_model)
    corpus_tfidf = [tfidf_model[doc] for doc in corpus]
    print('TF-IDF:')
    for tfidf in corpus_tfidf:
        print(tfidf)


if __name__ == '__main__':
    run()