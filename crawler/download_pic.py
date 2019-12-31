import base64
import hashlib
import os
from io import BytesIO
import requests
from PIL import Image


def download_pic(url):
    pic_name = hashlib.md5(url.encode(encoding='UTF-8')).hexdigest()
    print(pic_name)
    response = requests.get(url)
    save_path = 'pics/' + pic_name + ".jpg"
    if os.path.exists(save_path):
        return "/"+save_path
    image = Image.open(BytesIO(response.content))
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image.save(save_path)
    return "/"+save_path

if __name__ == '__main__':
    download_pic("https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic81brEpWSkaxef79PKZ06cAHeOZBcBNjkib3vUoLGoRqctV0nSszuyUBIqvgzFOSXI5NVuqhRrFcYUQ/640?wx_fmt=jpeg")