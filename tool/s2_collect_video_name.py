import os
import random

dataset = 'multiface'

selected_num = 6 # 选取的视频数量

# 设置文件夹路径
# folder_path = f'render_video/{dataset}/Ours/test_B'
folder_path = f'user_study/multiface/CodeTalker'

# 设置输出文本文件的路径
output_file_path = f'selected_videoname/filenames_{dataset}.txt'

# 获取文件夹中所有文件和文件夹的名称
entries = os.listdir(folder_path)

#随机选取10个文件名，且不会重复
random_entries = random.sample(entries, min(selected_num, len(entries)))

# 打开文件准备写入
with open(output_file_path, 'w') as output_file:
    # 遍历所有条目
    for entry in random_entries:
        # 构建完整的文件或文件夹路径
        # full_entry_path = os.path.join(folder_path, entry)

        output_file.write(entry + '\n')

print(f"文件名已写入到文本文件 {output_file_path}。")