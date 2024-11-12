#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('lipsticks.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
# 统计各品牌平均折扣力度
discount = data.groupby(by='品牌').agg({'折扣':'mean'}).sort_values(by='折扣', ascending=False)[1:11]
plt.rcParams['font.sans-serif'] = 'SimHei'#显示中文
#柱状图
plt.bar(range(len(discount)),discount['折扣'])
plt.xticks(range(len(discount)),discount.index,rotation=100) #x轴刻度
plt.xlabel('品牌') #x轴标签
plt.ylabel('折扣力度') #y轴标签
plt.title('各品牌折扣力度统计柱状图') #标题
plt.show()
#统计各品牌销量
# brand = data['品牌'].value_counts()
#
# plt.figure(figsize=(10,8)) #设置画布大小
# #饼图
# plt.pie(brand, labels=brand.index, autopct='%.2f%%')
# plt.title('各品牌销量占比饼图') #标题
# plt.show()

