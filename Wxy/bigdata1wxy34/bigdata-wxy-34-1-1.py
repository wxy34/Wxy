import re

def parse_face_recognition_results(filename):
    """
    处理人脸识别结果文件，生成以照片编号为键、学号列表为值的字典。

    :param filename: 存有人脸识别结果的文件名
    :return: 字典，其中键为照片编号，值为识别到的一系列学号的列表
    """
    # 步骤（i）读取文件
    # a. 打开并读取文件
    data_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data_list = [line.strip() for line in file]
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return {}
    results_dict = {}
    for item in data_list:
        # 步骤（ii）&（iii）切割数据
        key_value_pair = item.rsplit('_', 1)  # 使用rsplit保留最后一个'_'
        image_id = key_value_pair[1].replace('.jpg', '')  # 提取照片编号
        student_ids_str = key_value_pair[0][1:-1]  # 去除方括号 '[' 和 ']'
        student_ids = re.findall(r"'(.*?)'", student_ids_str)  # 使用正则表达式提取学号
        # 步骤（iv）过滤掉无效的学号标识符'0'
        valid_student_ids = list(filter(lambda x: x != '0', student_ids))
        # 插入到字典中
        results_dict[image_id] = valid_student_ids
    return results_dict

# 调用函数，传入文件名
filename = '数据/dir_1000.txt'
results = parse_face_recognition_results(filename)
# 输出结果
print(results)