#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('zhaopin.xlsx')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#统计各学历的岗位需求量
# data_xueli = data['学历'].value_counts()
# plt.figure(figsize=(5,5))
# #饼图
# plt.pie(data_xueli, labels=data_xueli.index, autopct='%.2f%%', pctdistance=0.8)
# plt.title('各学历的岗位需求量占比饼图') #标题
# plt.show()
#统计岗位对不同工作经验的需求量
data_jingyan = data['工作经验要求'].value_counts().sort_index()
#柱状图
plt.bar(range(len(data_jingyan)),data_jingyan)
plt.xticks(range(len(data_jingyan)),data_jingyan.index, rotation=45) #x轴刻度
plt.xlabel('工作经验') #x轴标签
plt.ylabel('需求量',) #y轴标签
for i,j in zip(range(len(data_jingyan)),data_jingyan):
    plt.text(i, j, '%d'%j, ha='center', va='bottom') #添加数据标签
plt.title('经验的岗位需求量') #标题
plt.show()

