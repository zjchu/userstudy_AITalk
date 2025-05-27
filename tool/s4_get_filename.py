import os

dataset = "vocaset"

folder_list = {
    f"user_study/{dataset}/CodeTalker",
    f"user_study/{dataset}/FaceFormer",
    f"user_study/{dataset}/GT",
    f"user_study/{dataset}/MeshTalk",
    f"user_study/{dataset}/voca",
    f"user_study/{dataset}/CorrTalk",
    f"user_study/{dataset}/DiffSpeaker",
    f"user_study/{dataset}/TalkingStyle",
    f"user_study/{dataset}/FaceDiffuser",
}


for folder_path in folder_list:
    # 获取文件夹中的文件名列表
    file_names = os.listdir(folder_path)
    # 确定文本文件的路径：如multiface_codetalker
    txt_file_name = "_".join(folder_path.split("/")[1:])
    # txt文件路径
    os.makedirs('filename', exist_ok=True)
    txt_file_path = fr"filename/{txt_file_name}.txt"
    # 打开txt文件并写入文件名
    with open(txt_file_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(folder_path + '/' + file_name + '\n')


