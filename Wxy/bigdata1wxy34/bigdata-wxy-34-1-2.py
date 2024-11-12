# 导入所需的库
import os

# 定义文件路径
input_file_path = '数据/Grid_solar_EV_data.txt'
ny_output_file = '数据/1-NY.txt'
austin_output_file = '数据/1-Austin.txt'
boulder_output_file = '数据/1-Boulder.txt'

# (i) 读取文件
with open(input_file_path, 'r', encoding='utf-8') as file:
    # 按行读取内容
    lines = file.readlines()

# (ii) 数据分割
data = [line.strip().split('\t') for line in lines]

# (iii) 列表存储数据
ny_data = []
austin_data = []
boulder_data = []

# 循环遍历列表，将属于不同城市的数据存储进对应空列表
for row in data:
    if row[0].startswith('NY'):
        ny_data.append(row)
    elif row[0].startswith('Austin'):
        austin_data.append(row)
    elif row[0].startswith('Boulder'):
        boulder_data.append(row)

# (iv) 保存文件
def save_to_file(data_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for row in data_list:
            file.write('\t'.join(row) + '\n')

# 保存每个城市的数据到对应的文件
save_to_file(ny_data, ny_output_file)
save_to_file(austin_data, austin_output_file)
save_to_file(boulder_data, boulder_output_file)

print("数据已成功分割并保存到文件中。")