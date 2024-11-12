import requests
from bs4 import BeautifulSoup
import json
urls=[]
for i in range(1,5):
    url=( 'http://www.tipdm.com/qyfw/index_'+str(i)+'.jhtml')
    urls.append(url)
dic={}
header={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
for j in range(4):
        html = requests.get(urls[j])
        soup = BeautifulSoup(html.text, 'lxml')
        title= soup.find_all('h1')
        conect=soup.find_all(attrs={'class':'des'})
        for k,v in zip(title,conect):
            dic[k.get_text()]=v.get_text()
with open('data4.json', 'w',encoding='utf-8') as f:
    json.dump(dic,f, ensure_ascii=False, indent=4)