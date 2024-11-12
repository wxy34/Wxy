#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('tmall_order_report.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
# chengjiao = len(data.loc[data['退款金额'] == 0, '退款金额']) #成交订单量
# tuikuan = len(data) - chengjiao #退款订单量
# plt.figure(figsize=(4,4)) #设置画布
# #饼图
# plt.pie([chengjiao, tuikuan], labels=['成交订单量', '退款订单量'], autopct='%.2f%%')
# plt.title('成交订单量、退款订单量占比饼图') #标题
# plt.show()
#提取各地点的订单数
area = data['收货地址'].value_counts()
#柱状图
plt.bar(range(len(area)), area)
plt.xticks(range(len(area)), area.index, rotation=90) #x轴刻度
plt.xlabel('地点') #x轴标签
plt.ylabel('订单数') #y轴标签
plt.title('订单地点分布柱状图') #标题
plt.show()
