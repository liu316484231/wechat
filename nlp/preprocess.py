import codecs
import re

import jieba as jieba


class PreProcess():
    stopwords = []
    stopword_filepath="./stopwordList/stopword.txt"
    def __init__(self):
        self.__readin_stop()
    def __readin_stop(self):
        file_obj = codecs.open(self.stopword_filepath,'r','utf-8')
        while True:
            line = file_obj.readline()
            line=line.strip('\r\n')
            if not line:
                break
            self.stopwords.append(line)
        file_obj.close()
    def clean_doc(self,doc):
        # 汉字的Unicode范围为4e00-9fa5
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        filter_data = re.findall(pattern,doc)
        cleaned_doc = ''.join(filter_data)
        return cleaned_doc
    def cut(self,doc):
        seg = jieba.cut(doc)
        results = []
        for item in seg:
            if item in self.stopwords:
                continue
            results.append(item)
        return results