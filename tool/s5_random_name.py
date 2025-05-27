import os
import random

dataset='multiface'

if dataset =='multiface':
    num_videos = 18
elif dataset == 'vocaset':
    num_videos = 20
elif dataset =="BIWI":
    num_videos = 20

file_list = [
    f"{dataset}_voca.txt",
    f"{dataset}_meshtalk.txt",
    f"{dataset}_faceformer.txt",
    f"{dataset}_codetalker.txt",
    f"{dataset}_corrtalk.txt",
    f"{dataset}_diffspeaker.txt",
    f"{dataset}_talkingstyle.txt",
    f"{dataset}_facediffuser.txt",
    f"{dataset}_gt.txt"
]


out_filename = f'filenames_{dataset}_after.txt'
# 创建结果文件filenames.txt
result_file = open(out_filename, 'w')

selected_name = []
# 每个方法选择18个视频
for _ in range(num_videos):
    # 创建一个空的列表用于存放已经取出的行
    selected_lines = []

    for file in file_list:
        with open('filename/' + file, 'r') as f:   #不区分大小写
            lines = f.readlines()
        selected_line = random.sample(lines, 1)  # 随机取出1行
        if selected_line in selected_name:
            while True:
                selected_line = random.sample(lines, 1)
                if not selected_line in selected_name:
                    break

        selected_name.append(selected_line) # 将此行存入列表中
        selected_lines.extend(selected_line)  # 将选中的行添加到列表中

     # 将选中的行写入结果文件
    result_file.writelines(selected_lines)


def check_duplicate_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    string_dict = {}

    for index, line in enumerate(lines):
        string = line.strip()
        if string in string_dict:
            string_dict[string].append(index + 1)
        else:
            string_dict[string] = [index + 1]

    # 检查是否存在重复行
    duplicates_exist = False

    for string, line_numbers in string_dict.items():
        if len(line_numbers) > 1:
            duplicates_exist = True
            print(f'重复的字符串 "{string}" 在以下行中出现：{line_numbers}')

    if not duplicates_exist:
        print("文件中每一行都是唯一的，没有重复行")

check_duplicate_lines(out_filename)