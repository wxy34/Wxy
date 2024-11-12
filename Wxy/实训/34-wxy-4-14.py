#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('car_selling_fact.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#统计各省份的汽车销售量
# province_sales = data.groupby(by = data['省份']).agg({'销量':'sum'}).sort_values(by='销量', ascending=False)
# #柱状图
# plt.bar(range(len(province_sales)), province_sales['销量'])
# plt.xticks(range(len(province_sales)), province_sales.index) #x轴刻度
# plt.xlabel('省份') #x轴标签
# plt.ylabel('销售量') #y轴标签
# plt.title('各省份的汽车销售量分布柱状图') #标题
# plt.show()
#统计各车系的汽车销售量
cars_sales = data.groupby(by=data['车系']).agg({'销量':'sum'}).sort_values(by='销量', ascending=False)

plt.figure(figsize=(5,5)) #设置画布大小
#饼图
plt.pie(cars_sales['销量'], labels=cars_sales.index, autopct='%.2f%%')
plt.title('各车系销售量占比饼图') #标题
plt.show()

