import urllib3
from lxml import etree
import json
urls = []
for i in range(1,5):
    url = 'http://tipdm.com/xwzx/index_'+str(i)+'.jhtml'
    urls.append(url)
urls
all_data = {}
for j in range(len(urls)):
    http = urllib3.PoolManager()
    rq = http.request('GET', urls[j])
    html = etree.HTML(rq.data, parser=etree.HTMLParser(encoding='utf-8'))
    title = html.xpath('//*[@id="t505"]/div/div[3]/h1/a/text()')
    content = html.xpath('//*[@id="t505"]/div/div[3]/div/text()')
    for i in range(len(title)):
        all_data[title[i]] = content[i]
with open('data8', 'w',encoding='utf-8') as f_obj:
    json.dump(all_data ,f_obj, ensure_ascii=False, indent=4)