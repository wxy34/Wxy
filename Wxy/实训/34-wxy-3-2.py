import urllib3

http = urllib3.PoolManager()
url = 'http://tipdm.com/'
rq = http.request('GET',url)

print('服务器响应码:',rq.status)
from bs4 import BeautifulSoup

html = rq.data.decode('utf-8')
soup = BeautifulSoup(html,'lxml')

 # 产品中心
chanpin = soup.find('ul',id='sub248').get_text().strip('\n').split('\n')
# 实验室建设
shiyanshi= soup.find('ul',id='sub496').get_text().strip('\n').split('\n')
# 培训认证
peixun= soup.find('ul',id='sub244').get_text().strip('\n').split('\n')
# 企业应用
qiye= soup.find('ul',id='sub474').get_text().strip('\n').split('\n')
# 校企合作
xiaoqi= soup.find('ul',id='sub475').get_text().strip('\n').split('\n')
# 新闻中心
xinwen= soup.find('ul',id='sub505').get_text().strip('\n').split('\n')
# 关于我们
guanyu= soup.find('ul',id='sub254').get_text().strip('\n').split('\n')

#整理数据
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
