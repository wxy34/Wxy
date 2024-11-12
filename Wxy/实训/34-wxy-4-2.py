#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('douban.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#统计各评分分布
# num = data['评分'].value_counts()
# #饼图
# plt.pie(num, autopct='%.2f %%', labels=num.index)
# plt.title('《流浪地球》豆瓣评分分布饼图') #标题
# plt.show()
#提取评论数量最多的前5个城市数据
citys_data = data['居住城市'].value_counts()[:5]
#柱状图
plt.bar(range(len(citys_data)),citys_data)
plt.xticks(range(len(citys_data)),citys_data.index) #x轴刻度
plt.xlabel('城市') #x轴标签
plt.ylabel('评论数量') #y轴标签
plt.title('评论数量最多的前5个城市排名柱状图') #标题
plt.show()
