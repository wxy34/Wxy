#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('titanic.xlsx')#正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# #统计男女乘客比例
# sex = data['sex'].value_counts()
# #饼图
# plt.pie(sex,labels=sex.index, autopct='%.2f%%')
# plt.title('男女乘客比例饼图') #标题
# plt.show()
#统计船票价格分布
fare_section = data['fare_section'].value_counts()
#柱状图
plt.bar(range(len(fare_section)),fare_section)
plt.xticks(range(len(fare_section)),fare_section.index) #x轴刻度
plt.xlabel('船票价格分布') #x轴标签
plt.ylabel('频数') #y轴标签
plt.title('船票价格分布柱状图') #标题
plt.show()

