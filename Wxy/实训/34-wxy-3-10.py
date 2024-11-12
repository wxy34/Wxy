import requests
import re
import json
urls = []
for i in range(1,5):
    url = 'http://tipdm.com/xqhz/index_'+str(i)+'.jhtml'
    urls.append(url)
lists={}
header={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
for j in range(4):
    http=requests.get(urls[j],headers=header)
    a = re.compile('<h1><a href=.*? target="_blank">(.*?)</a></h1>', re.S)
    b = re.compile('<div class="des">(.*?)</div>', re.S)
    title = a.findall(http.text)
    conect = b.findall(http.text)
    for i,name in enumerate(title):
        intro = conect[i]
        lists[name] = intro
with open('data10', 'w',encoding='utf-8') as f:
    json.dump(lists,f, ensure_ascii=False, indent=4)