#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('book.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#提取作品数量最多的前10位作者排名
# author = data.groupby(by='作者').size().sort_values(ascending=False)[1:11]
# #柱状图
# plt.bar(range(len(author)),author)
# plt.xticks(range(len(author)),author.index) #x轴刻度
# for i,j in zip(range(len(author)),author):
#     plt.text(i,j,'%d'%j,ha='center',va='bottom') #添加数据标签
# plt.title('作品数量最多的前10位作者排名柱状图') #标题
# plt.xlabel('作者') #x轴标签
# plt.ylabel('作品数') #y轴标签
# plt.show()
#统计评分分布
pingfen = data['评分区间'].value_counts().sort_index()
plt.figure(figsize=(6,6))
#饼图
plt.pie(pingfen, labels=pingfen.index, autopct='%.2f%%')
plt.title('豆瓣图书评分分布饼图') #标题
plt.show()

