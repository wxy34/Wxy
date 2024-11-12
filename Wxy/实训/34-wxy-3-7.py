import requests
from bs4 import BeautifulSoup
import json
urls = []
for i in range(1,5):
    url = 'http://tipdm.com/xwzx/index_'+str(i)+'.jhtml'
    urls.append(url)
urls
data = {}
for j in range(len(urls)):
    rq = requests.get(urls[j])
    soup = BeautifulSoup(rq.text, 'lxml')
    all_content = soup.find('section',id="t505").find_all('div',class_="item clearfix")
    for i in range(len(all_content)):
        title = all_content[i].h1.text
        content = all_content[i].find('div',class_="des").text
        data[title]= content
with open('data7', 'w',encoding='utf-8') as f:
    json.dump(data ,f, ensure_ascii=False, indent=4)