urls = []
for i in range(1,5):
    url = 'http://www.tipdm.com/qyfw/index_'+str(i)+'.jhtml'
    urls.append(url)
urls
import urllib3
from lxml import etree
all_data = {}
for j in range(len(urls)):
    http = urllib3.PoolManager()
    rq = http.request('GET', urls[j])
    html = etree.HTML(rq.data, parser=etree.HTMLParser(encoding='utf-8'))
    ye_title = html.xpath('//*[@id="t474"]/div/div/h1/a/text()')
    ye_content = html.xpath('//*[@id="t474"]/div/div/div/text()')
    for i in range(len(ye_title)):
        all_data[ye_title[i]] = ye_content[i]
import json
with open('data5', 'w',encoding='utf-8') as f_obj:
    json.dump(all_data ,f_obj, ensure_ascii=False, indent=4)