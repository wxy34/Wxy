import requests

url = 'http://tipdm.com/'
rq = requests.get(url)
print('状态码:', rq.status_code)
from lxml import etree

html = etree.HTML(rq.content, parser=etree.HTMLParser(encoding='utf-8'))

# 产品中心
chanpin = html.xpath('//*[@id="sub248"]/li/a/text()')
# 实验室建设
shiyanshi = html.xpath('//*[@id="sub496"]/li/a/text()')
# 培训认证
peixun = html.xpath('//*[@id="sub244"]/li/a/text()')
# 企业应用
qiye = html.xpath('//*[@id="sub474"]/li/a/text()')
# 校企合作
xiaoqi = html.xpath('//*[@id="sub475"]/li/a/text()')
# 新闻中心
xinwen = html.xpath('//*[@id="sub505"]/li/a/text()')
# 关于我们
guanyu = html.xpath('//*[@id="sub254"]/li/a/text()')
data = {'产品中心':chanpin,
              '实验室建设':shiyanshi,
              '培训认证':peixun,
              '企业应用':qiye,
              '校企合作':xiaoqi,
              '新闻中心':xinwen,
              '关于我们':guanyu}

import json

with open('data.json', 'w',encoding='utf-8') as f_obj:
    # 使用函数json.dump()将数据存储到文件中
    json.dump(data ,f_obj, ensure_ascii=False, indent=4)

