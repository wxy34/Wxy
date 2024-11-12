import requests
from bs4 import BeautifulSoup
import json
urls = []
for i in range(1,5):
    url = 'http://tipdm.com/xqhz/index_'+str(i)+'.jhtml'
    urls.append(url)
urls
data = {}
for j in range(len(urls)):
    rq = requests.get(urls[j])
    soup = BeautifulSoup(rq.text, 'lxml')
    all_content = soup.find('section',id="t475").find_all('div',class_="con")
    for i in range(len(all_content)):
        data [all_content[i].h1.text] = all_content[i].find('div', class_="des").text
with open('data9', 'w',encoding='utf-8') as f:
    json.dump(data ,f, ensure_ascii=False, indent=4)