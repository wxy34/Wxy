#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('vending_machine.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#2017年6月销量前5的商品
# yuefen_6_top5 = data.loc[data['支付月份'] == 6, '商品'].value_counts()[:5]
# #柱状图
# plt.bar(range(5),yuefen_6_top5)
# plt.xticks(range(5),yuefen_6_top5.index,rotation=45) #x轴刻度
# plt.xlabel('商品') #x轴标签
# plt.ylabel('销量') #y轴标签
# for i,j in zip(range(5),yuefen_6_top5):
#     plt.text(i, j, '%d'%j, ha='center', va='bottom') #添加数据标签
# plt.title('2017年6月销量前5的商品销量柱状图') #标题
# plt.show()
#统计每台售货机总交易额
num = data.groupby(by='地点').agg({'实际金额':'sum'})
#饼图
plt.pie(num['实际金额'], labels=num.index, autopct='%.2f%%')
plt.title('每台售货机总交易额占比饼图') #标题
plt.show()

