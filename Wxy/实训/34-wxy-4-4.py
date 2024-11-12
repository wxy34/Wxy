#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('supermarket_sales.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#各月销售金额统计
# yue_money = data.groupby('销售月份').agg({'销售金额':sum})
# plt.figure(figsize=(5,5))
# #饼图
# plt.pie(yue_money['销售金额'], labels=yue_money.index, autopct='%.2f%%')
# plt.title('该超市各月销售金额占比饼图') #标题
# plt.show()
#促销商品月销售金额统计
cuxiao = data[data['是否促销']=='是'].groupby('销售月份').agg({'销售金额':sum})
#柱状图
plt.bar(range(len(cuxiao)),cuxiao['销售金额'])
plt.xticks(range(len(cuxiao)),cuxiao.index) #x轴刻度
plt.xlabel('销售月份') #x轴标签
plt.ylabel('月销售金额') #y轴标签
plt.title('促销商品月销售金额柱状图') #标题
plt.show()


