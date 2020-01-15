from pypinyin import lazy_pinyin
from util.chinese_translate import chs_to_cht


def process_data_index(list):
    new_list = []
    for item in list:
        new_list.append({
            'id': item['id'],
            'title': chs_to_cht(item['title'])[:20],
            'class': item['class'],
            'digest': chs_to_cht(item['digest'])[:20] + "...",
            'cover': item['cover']
        })
    return new_list

def hanzi_to_pinyin(hanzi):
    pinyin = "".join(lazy_pinyin('刘冰'))
    return pinyin