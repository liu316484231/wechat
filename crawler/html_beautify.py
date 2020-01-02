from bs4 import BeautifulSoup

from crawler.download_pic import download_pic
from util.chinese_translate import chs_to_cht


def beautify(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find(id="js_content")
    div['id'] = "my_content"
    del div['class']
    del div['style']

    print(str(soup))
    img_list = soup.find_all("img")
    for img in img_list:
        src = img['data-src']
        save_path = download_pic(src)
        img['data-src'] = save_path
        img['src'] = save_path

    sec_list = soup.find_all("section")
    for sec in sec_list:
        del sec['powered-by']

    format_html = str(soup.find(id='my_content'))
    print(format_html)
    return format_html

if __name__ == "__main__":
    print("go..")
    html = '<div class="rich_media_content" id="js_content" style="visibility: hidden;"> \
<section style="box-sizing: border-box;font-size: 16px;"><section class="horizontal-tb tn-yzk-fuid-text-54317-1565447594790" powered-by="xiumi.us" style="text-align: right;font-size: 12px;line-height: 1;box-sizing: border-box;"><p style="box-sizing: border-box;"><span style="font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">▲ 点击上方蓝字，关注<span style="color: rgb(200, 145, 64);box-sizing: border-box;">外婆的灶台</span>，第 <strong style="box-sizing: border-box;">122</strong> 餐</span></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.4048583" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic828L8GvyjpyohxYREMbH6wtHBvSB0tsHibFozgSnGXTicRmB8ic1HUr59Eics5YWs45GibbXTGHAiaibDg7g/640?wx_fmt=jpeg" data-type="jpeg" data-w="988" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5625" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic828L8GvyjpyohxYREMbH6wtP0VwsuHgOCiatU8tFpt8QWfr6b2rtTqNFSdY1Liax9RgemQqUwhJt1Vg/640?wx_fmt=jpeg" data-type="jpeg" data-w="800" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;line-height: 1.8;letter-spacing: 1.5px;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="text-align: center;white-space: normal;box-sizing: border-box;"><span style="font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">∞</span></p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;">不夸张地说，在冬天大白菜是东北人的本命。<br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;">随着装满白菜的卡车驶进小区，大喇叭循环高喊：“白菜贱卖！！白菜贱卖！！白菜贱卖！！”大妈们肘挎编织袋、手推拉杆车、带上自家大爷......东北的初冬以大爷大妈们撸袖子抢大白菜正式开始。<br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;">卖白菜的大哥也是颇有特色，讲究的就是俩字：“豪迈！”什么叫豪卖？就是五十斤以下不卖。记得我之前就在大卡车前要称一颗白菜，喊了半天，大哥就是目光所及之处没有你。现在想来那应该是个性温和的大哥，实在不想跟年轻人理论一颗白菜够干啥的。</p><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p><p style="white-space: normal;box-sizing: border-box;">其实一方水土养一方人，上百年传下来的东西是根深蒂固的。虽然我们这代年轻人已经没有储秋菜的习惯，但是看着家里长辈囤白菜、晒白菜、腌酸菜，也是一件很有仪式感的事情。不可否认，这又是一个被大白菜支配的冬天。</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1472785" data-src="https://mmbiz.qpic.cn/mmbiz_png/CJsk4EDdic828L8GvyjpyohxYREMbH6wtgAzKt6MZwV1u7lv8yN13ZuicbGKILE7ardibye4uoh9RYgNKtqAcZykg/640?wx_fmt=gif" data-type="gif" data-w="2811" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb tn-yzk-fuid-text-94930-1572443778354" powered-by="xiumi.us" style="text-align: center;font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;"><p style="box-sizing: border-box;"><em style="box-sizing: border-box;"><strong style="box-sizing: border-box;">白菜◦300g / 五花肉◦100g</strong></em></p><p style="box-sizing: border-box;"><em style="box-sizing: border-box;"><strong style="box-sizing: border-box;">泡发木耳◦100g / 泡软粉条◦150g</strong></em></p><p style="box-sizing: border-box;"><em style="box-sizing: border-box;"><strong style="box-sizing: border-box;">葱◦16g / 蒜◦2瓣 / 小米辣◦1根</strong></em></p><p style="box-sizing: border-box;"><em style="box-sizing: border-box;"><strong style="box-sizing: border-box;">花椒◦10颗 / 八角◦1个 / 姜◦4g</strong></em></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5625" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic828L8GvyjpyohxYREMbH6wtQict9K8Odics6Gs2bCv1u0vtpXCI6jvavsIHGdTYyGhat3RHLIXj4pwQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="800" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 13px;color: rgb(200, 145, 64);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">∆ 白菜帮斜切，即刀与白菜帮呈30度角切下去。斜切可以把白菜帮切薄，易熟也更入味儿。白菜叶手撕成块，帮和叶分开装。</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 13px;color: rgb(200, 145, 64);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">∆ 提前将木耳泡发，粉条泡软。五花肉、蒜切片，葱切葱花，姜切丝。</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1472785" data-src="https://mmbiz.qpic.cn/mmbiz_png/CJsk4EDdic828L8GvyjpyohxYREMbH6wtKvrZBeGXRKywZDcZRccsibCQ9tg2sa0sGiaLqYCTic5NVsaCvWJPEkNyg/640?wx_fmt=gif" data-type="gif" data-w="2811" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 13px;box-sizing: border-box;"><p style="text-align: center;white-space: normal;box-sizing: border-box;">❶</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">锅中无油，加入五花肉煸出油，煎至双面焦黄。</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5561905" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtTLGJDqlCQwXPZVJeaUmtcvXzEn5sMR9TYY93qf9DW9ejib3ckXicjbOw/640?wx_fmt=gif" data-type="gif" data-w="525" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 13px;color: rgb(200, 145, 64);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">∆ 带皮五花做炖菜口感很Q弹，但猪皮在煸油的过程中会溅油。锅盖可以盖上一半，切记不要全部盖上，不然形成水蒸气流进油锅里....那就更热闹了。</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="text-align: center;font-size: 13px;box-sizing: border-box;"><p style="box-sizing: border-box;">❷</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">加入花椒、八角、葱花、姜丝、蒜末，翻炒炝香。</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5561905" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtgzXU0jibCrtYMvbyia4oAl7MfLxbHy2sGJhoarlIhEdKickicbZykXcCPw/640?wx_fmt=gif" data-type="gif" data-w="525" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="text-align: center;font-size: 14px;box-sizing: border-box;"><p style="box-sizing: border-box;">❸</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">加入白菜帮翻炒，淋入一汤勺水，加盖焖煮10分钟，开盖加入白菜叶翻炒均匀。</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5625" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic828L8GvyjpyohxYREMbH6wtxesqUyVLGI2tQygVASialDknuS9wx6rN9UIKWfBGkDl12ibawg0LeiaXg/640?wx_fmt=jpeg" data-type="jpeg" data-w="800" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="text-align: center;font-size: 13px;box-sizing: border-box;"><p style="box-sizing: border-box;">❹</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">加入十三香半茶匙，酱油1汤匙，蚝油2汤匙，盐1茶匙，翻炒均匀，加入700ml清水。</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5561905" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtEBLQkW7tGcXf5ZeGINNic2rUQVwOwWVsAnRqCibCibzmpaaDtnPu0DwVw/640?wx_fmt=gif" data-type="gif" data-w="525" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="text-align: center;font-size: 13px;box-sizing: border-box;"><p style="box-sizing: border-box;">❺</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">水沸后加入粉条和木耳，将粉条煮至无硬芯。</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5561905" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtuNC0Jiac2MkksTjSMibkkgH9IYH6tjnjoP8XEajJOjoI09ibnaAXdOiaag/640?wx_fmt=gif" data-type="gif" data-w="525" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 13px;color: rgb(200, 145, 64);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">∆ 泡软的粉条不耐煮，很快就熟了，要注意火候哦。</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="text-align: center;font-size: 13px;box-sizing: border-box;"><p style="box-sizing: border-box;">❻</p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">尝下汤汁，根据咸淡适量加些盐。最后加入小米辣，鸡精半茶匙，出锅~</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.5561905" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtNHsIEdhyl2XN7iaAcFcEd3M4bEZP6CqMnnFaQBia5WsN8zUByFIaxeWQ/640?wx_fmt=gif" data-type="gif" data-w="525" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.1472785" data-src="https://mmbiz.qpic.cn/mmbiz_png/CJsk4EDdic828L8GvyjpyohxYREMbH6wtbYtSr4wdNUs8ssicrkrBWPr9bDWR28icc8N9JRvyh5cHr2vRLupZnN5g/640?wx_fmt=gif" data-type="gif" data-w="2811" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="font-size: 14px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;">爽滑劲道的红薯粉条吸饱了鲜醇汤汁，嗦上一口……嘶，果然是迎接冬天的必备味道！！！</p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 95%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.56125" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/CJsk4EDdic828L8GvyjpyohxYREMbH6wtz70RIGmHWHtkZTyW0tOVGV8dB8gSnaBlOPMdDWSDr5icOibrTTSEPH4g/640?wx_fmt=jpeg" data-type="jpeg" data-w="800" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb tn-yzk-fuid-text-65084-1530510974459" powered-by="xiumi.us" style="line-height: 1.1;letter-spacing: 1px;padding-right: 15px;padding-left: 15px;font-size: 10px;box-sizing: border-box;"><p style="text-align: right;white-space: normal;box-sizing: border-box;"><br/></p><p style="text-align: right;white-space: normal;box-sizing: border-box;"><span style="font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">文/编辑/拍摄 by 王干部</span></p><p style="text-align: right;white-space: normal;box-sizing: border-box;"><span style="font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">改刀/配菜/掌勺 by 王干部</span></p><p style="text-align: right;white-space: normal;box-sizing: border-box;"><span style="font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">品尝并拒绝刷碗 by 酸角小姐</span></p><p style="text-align: right;white-space: normal;box-sizing: border-box;"><span style="color: rgb(160, 160, 160);font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">©2019 All rights reserved</span></p><p style="text-align: right;white-space: normal;box-sizing: border-box;"><span style="color: rgb(160, 160, 160);font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;">[转载请通过公众号联系作者]</span></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.0277778" data-src="https://mmbiz.qpic.cn/mmbiz_png/CJsk4EDdic828L8GvyjpyohxYREMbH6wtjP6dOWibt2kmJtPu1dibCuoUhWUyttWKW0eX6JAaibicdH8KLbIuV4RAIQ/640?wx_fmt=png" data-type="png" data-w="1080" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section powered-by="xiumi.us" style="margin-top: 10px;margin-bottom: 10px;text-align: center;box-sizing: border-box;"><section style="display: inline-block;vertical-align: top;box-sizing: border-box;"><section class="horizontal-tb tn-yzk-fuid-text-85888-1568958288496" style="margin-bottom: -6px;line-height: 1em;padding-left: 2px;padding-right: 2px;color: rgb(3, 3, 3);font-size: 14px;font-family: Optima-Regular, PingFangTC-light;letter-spacing: 3px;box-sizing: border-box;"><p style="box-sizing: border-box;"><strong style="box-sizing: border-box;">也许你还想吃</strong></p></section><section style="width: 100%;height: 10px;background-color: rgba(255, 202, 0, 0.84);box-sizing: border-box;"></section></section></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;width: 40%;box-sizing: border-box;"><img class="raw-image" data-ratio="0.178125" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wtp6WhMA66ZaxZND2lNkD7ibyD3osia6uqajscWt5daWar7nRrHd0q0PFw/640?wx_fmt=gif" data-type="gif" data-w="640" style="vertical-align: middle;width: 100%;box-sizing: border-box;"/></section></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section class="horizontal-tb tn-yzk-fuid-text-45100-1572444122239" powered-by="xiumi.us" style="text-align: center;font-size: 13px;color: rgb(62, 62, 62);letter-spacing: 1.5px;line-height: 1.8;padding-right: 15px;padding-left: 15px;font-family: Optima-Regular, PingFangTC-light;box-sizing: border-box;"><p style="box-sizing: border-box;"><a data-itemshowtype="0" data-linktype="2" href="http://mp.weixin.qq.com/s?__biz=MzU0OTA0MjQ0Ng==&amp;mid=2247484129&amp;idx=1&amp;sn=4cc5ea67dfd4844b28230565939c476e&amp;chksm=fbb4a280ccc32b961b78f65d0676b8e222d833c4f2346bc21b1c6ea89aef4fd9d482038dfeb1&amp;scene=21#wechat_redirect" target="_blank">泡椒凤爪◦魔鬼的脚掌</a></p><p style="box-sizing: border-box;"><a data-itemshowtype="0" data-linktype="2" href="http://mp.weixin.qq.com/s?__biz=MzU0OTA0MjQ0Ng==&amp;mid=2247484104&amp;idx=1&amp;sn=174ce6a645c14924e5e9d1550f7ff52f&amp;chksm=fbb4a2a9ccc32bbf19b3b1910e28ca527825ea642625f4fa8a1dd1b24f816e1999c9b817f859&amp;scene=21#wechat_redirect" target="_blank">热干面◦入口觉滑,咽后觉润</a></p><p style="box-sizing: border-box;"><a data-itemshowtype="0" data-linktype="2" href="http://mp.weixin.qq.com/s?__biz=MzU0OTA0MjQ0Ng==&amp;mid=2247484098&amp;idx=1&amp;sn=ff7aefecaafdaaa55d86de122f3d054f&amp;chksm=fbb4a2a3ccc32bb53eff18f1c2588739d28cdf1222c1fcf0f0ee3fc7aec14693f5c28b3e2ed7&amp;scene=21#wechat_redirect" target="_blank">肥牛饭◦甩快餐外食好几条街</a></p><p style="box-sizing: border-box;"><a data-itemshowtype="0" data-linktype="2" href="http://mp.weixin.qq.com/s?__biz=MzU0OTA0MjQ0Ng==&amp;mid=2247484123&amp;idx=1&amp;sn=fa5ab851beaa7bc455e77869614808e3&amp;chksm=fbb4a2baccc32bacebb3fb7299ff11d4fb6412d1cb06beb4525573263ff3bd6758a3bc1bf21c&amp;scene=21#wechat_redirect" target="_blank">八珍豆腐◦让你再添一碗饭</a></p></section><section class="horizontal-tb" powered-by="xiumi.us" style="box-sizing: border-box;"><p style="white-space: normal;box-sizing: border-box;"><br style="box-sizing: border-box;"/></p></section><section powered-by="xiumi.us" style="text-align: center;margin-top: 10px;margin-bottom: 10px;box-sizing: border-box;"><section style="max-width: 100%;vertical-align: middle;display: inline-block;line-height: 0;box-sizing: border-box;"><img class="raw-image" data-ratio="0.9599178" data-src="https://mmbiz.qpic.cn/mmbiz_gif/CJsk4EDdic828L8GvyjpyohxYREMbH6wt84ibCJpR7MXKCiaHQBTqvLmFvFbATuAacKQEIqrDfkjIP6o2eVjGNRtw/640?wx_fmt=gif" data-type="gif" data-w="973" style="vertical-align: middle;box-sizing: border-box;"/></section></section><section class="horizontal-tb tn-yzk-fuid-text-79362-1570754504538" powered-by="xiumi.us" style="text-align: right;font-size: 12px;color: rgb(200, 145, 64);font-family: Optima-Regular, PingFangTC-light;line-height: 0;box-sizing: border-box;"><p style="box-sizing: border-box;"><strong style="box-sizing: border-box;">你在看吗？（右手放耳边做喇叭状）</strong></p></section></section> \
</div>'
    beautify(html)