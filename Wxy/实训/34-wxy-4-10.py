#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('travel.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
plt.figure(figsize=(5,5))
#统计出游同伴选择数据
# people = data['人物'].value_counts()
# #饼图
# plt.pie(people,labels=people.index,autopct='%.2f%%')
# plt.title('出游同伴选择统计饼图') #标题
# plt.show()
#提取前10个旅游热门景点
area = data['相关目的地'].value_counts()[:10]
#柱状图
plt.bar(range(len(area)),area)
plt.xticks(range(len(area)),area.index) #x轴刻度
plt.xlabel('目的地') #x轴标签
plt.ylabel('旅游人次') #y轴标签
plt.title('前10个旅游热门景点的排名柱状图') #标题
plt.show()
