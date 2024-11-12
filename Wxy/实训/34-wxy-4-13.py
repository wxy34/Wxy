#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('guomin.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#提取2000年第一季度各行业国民生产总值
# num1 = data.iloc[0, 5:]
# #重新设置标签
# label = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其他']
# plt.figure(figsize=(6,6))
# plt.pie(num1, labels=label, autopct='%.2f%%')
# plt.title('2000年第一季度国民生产总值行业构成分布饼图') #标题
# plt.show()
#提取2017年第一季度各产业国民生产总值
num = data.iloc[68, 2:5]
#柱状图
plt.bar(range(len(num)), num)
plt.xticks(range(len(num)),num.index,rotation=45) #x轴刻度
plt.xlabel('产业') #x轴标签
plt.ylabel('增加值') #y轴标签
plt.title('2017年第一季度各产业国民生产总值柱状图') #标题
plt.show()

