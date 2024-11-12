#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('HR_comma_sep.csv')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#各工资等级
# salary = data['salary'].value_counts()
# #饼图
# plt.pie(salary, labels=salary.index, autopct='%.2f%%')
# plt.title('各工资等级占比饼图') #标题
# plt.show()
#工资等级为“high”的工龄分布
high_time = data.loc[data['salary'] == 'high', 'time_spend_company'].value_counts().sort_index()
#柱状图
plt.bar(range(len(high_time)),high_time)
plt.xticks(range(len(high_time)),high_time.index) #x轴刻度
plt.xlabel('工龄') #x轴标签
plt.ylabel('频数') #y轴标签
plt.title('工资等级为“high”时的工龄分布柱状图') #标题
plt.show()

