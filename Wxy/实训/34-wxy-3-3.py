# import requests
# import json
# import re
#
# #导航条中的下拉菜单内容
# url = 'http://tipdm.com/'
# rq = requests.get(url)
# # print('状态码:', rq.status_code)
# # print('网页内容：\n',rq.text)
#
# caidan_com = re.compile(r'<li class=""><a href="http://tipdm.com:80/.*/index.jhtml" target="">(.*)</a></li>',re.I|re.M)
# caidan = re.findall(caidan_com,rq.text)
#
# with open('data1.json', 'w',encoding='utf-8') as f_obj:
#     # 使用函数json.dump()将数据存储到文件中
#     json.dump(caidan ,f_obj, ensure_ascii=False, indent=4)

# import requests
#
# url = 'http://tipdm.com/'
# response = requests.get(url)
# print(response.status_code)
# import requests
# import re
#
# url = 'http://tipdm.com/'
# response = requests.get(url)
# html_content = response.text
#
# # 编写正则表达式匹配导航条中的下拉菜单内容
# pattern = r'<a href="#">(.+?)</a>'
# menu_items = re.findall(pattern, html_content)
#
# print(menu_items)
# import requests
# import re
# import json
#
#
# url = 'http://tipdm.com/'
# rq = requests.get(url)
#
#
# caidan_com = re.compile(r'<li class=""><a href="http://tipdm.com:80/.*/index.jhtml" target="">(.*)</a></li>',re.I|re.M)
# caidan = re.findall(caidan_com,rq.text)
#
#
# with open('data.json', 'w',encoding='utf-8') as f_obj:
#     # 使用函数json.dump()将数据存储到文件中
#     json.dump(caidan ,f_obj, ensure_ascii=False, indent=4)




import requests
import re
import json
header={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
url = 'http://tipdm.com/'
res=requests.get(url,headers=header)
print('状态码:', res.status_code)
print('网页内容：\n',res.text)
a=re.compile('<a href=".*" target="">(.*)</a></li>',re.I|re.M)
data=re.findall(a,res.text)
with open('data2', 'w',encoding='utf-8') as f:
    json.dump(data ,f, ensure_ascii=False, indent=4)

