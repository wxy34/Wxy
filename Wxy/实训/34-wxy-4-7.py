#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('movies.csv')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#统计知名度排在前10的电影
# popul_10 = data[['popularity','original_title']].sort_values('popularity',ascending=False)[:10]
# #柱状图
# plt.bar(range(10),popul_10['popularity'])
# plt.xticks(range(10),popul_10['original_title'],rotation=90) #x轴刻度
# plt.xlabel('电影名称') #x轴标签
# plt.ylabel('知名度') #y轴标签
# for i,j in zip(range(10),popul_10['popularity']):
#     plt.text(i, j, '%d'%j, ha='center', va='bottom') #添加数据标签
# plt.title('知名度最高的前10部电影排名柱状图') #设置标题
# plt.show()
#对电影类别进行频数统计
liebie = data['genres'].apply(lambda x:x.split('|')[0]).value_counts()

plt.figure(figsize=(6,6)) #设置画布大小
#饼图
plt.pie(liebie, autopct='%.2f %%', labels=liebie.index,pctdistance=0.8)
plt.title('电影各类别占比饼图') #标题
plt.show()

