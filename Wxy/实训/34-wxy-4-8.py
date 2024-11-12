#读取数据
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('mum_baby_trade_history.csv')
plt.rcParams['font.sans-serif'] = 'SimHei'#正常显示中文
#统计各大类商品销量
# buy_cat1 = data.groupby(by='cat1').agg({'buy_mount':'sum'}).sort_values(by='buy_mount')
# #饼图
# plt.pie(buy_cat1['buy_mount'], labels=buy_cat1.index, autopct='%.2f%%')
# plt.title('各大类商品销量占比饼图') #标题
# plt.show()
# 人均大类购买情况
cat_aver_user = data.groupby('cat1')['buy_mount'].sum() / data.groupby('cat1')['user_id'].count()

#柱状图
plt.bar(range(len(cat_aver_user)),cat_aver_user)
plt.xticks(range(len(cat_aver_user)),cat_aver_user.index) #x轴刻度
plt.xlabel('商品大类') #x轴标签
plt.ylabel('人均购买量') #y轴标签
plt.title('各大类商品人均购买量柱状图') #标题
plt.show()
