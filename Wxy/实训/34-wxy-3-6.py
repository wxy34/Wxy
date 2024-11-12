import requests
import re
import json
urls = []
for i in range(1,5):
    url = 'http://www.tipdm.com/qyfw/index_'+str(i)+'.jhtml'
    urls.append(url)
lists={}
header={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
for j in range(4):
    http=requests.get(urls[j],headers=header)
    a=re.compile('<h1><a href=.*? target="_blank">(.*?)</a></h1>', re.S)
    title=a.findall(http.text)
    b=re.compile('<div class="des">(.*?)</div>',re.S)
    conect = b.findall(http.text)
    for i in range(len(title)):
        lists[title[i]]=conect[i]
with open('data6', 'w',encoding='utf-8') as f:
    json.dump(lists,f, ensure_ascii=False, indent=4)