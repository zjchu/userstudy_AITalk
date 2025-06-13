import os

multiface_face = {
    "multiface_voca_ours_face": 0,
    "multiface_voca_voca_face": 0,
    "multiface_meshtalk_ours_face": 0,
    "multiface_meshtalk_meshtalk_face": 0,
    "multiface_faceformer_ours_face": 0,
    "multiface_faceformer_faceformer_face": 0,
    "multiface_codetalker_ours_face": 0,
    "multiface_codetalker_codetalker_face": 0,
    "multiface_corrtalk_ours_face": 0,
    "multiface_corrtalk_corrtalk_face": 0,
    "multiface_diffspeaker_ours_face": 0,
    "multiface_diffspeaker_gt_face": 0,
    "multiface_talkingstyle_ours_face": 0,
    "multiface_talkingstyle_gt_face": 0,
    "multiface_facediffuser_ours_face": 0,
    "multiface_facediffuser_gt_face": 0,
    "multiface_gt_ours_face": 0,
    "multiface_gt_gt_face": 0,
}

multiface_lip = {
    "multiface_voca_ours_lip": 0,
    "multiface_voca_voca_lip": 0,
    "multiface_meshtalk_ours_lip": 0,
    "multiface_meshtalk_meshtalk_lip": 0,
    "multiface_faceformer_ours_lip": 0,
    "multiface_faceformer_faceformer_lip": 0,
    "multiface_codetalker_ours_lip": 0,
    "multiface_codetalker_codetalker_lip": 0,
    "multiface_corrtalk_ours_lip": 0,
    "multiface_corrtalk_corrtalk_lip": 0,
    "multiface_diffspeaker_ours_lip": 0,
    "multiface_diffspeaker_gt_lip": 0,
    "multiface_talkingstyle_ours_lip": 0,
    "multiface_talkingstyle_gt_lip": 0,
    "multiface_facediffuser_ours_lip": 0,
    "multiface_facediffuser_gt_lip": 0,
    "multiface_gt_ours_lip": 0,
    "multiface_gt_gt_lip": 0,
}

keyname = {
    "voca": 0,
    "meshtalk": 1,
    "faceformer": 2,
    "codetalker": 3,
    'corrtalk': 4,
    'diffspeaker': 5,
    'talkingstyle': 6,
    'facediffuser': 7,
    'gt': 8,
}


multiface_realism = {
    "multiface_voca_realism": 0,
    "multiface_meshtalk_realism": 0,
    "multiface_faceformer_realism": 0,
    "multiface_codetalker_realism": 0,
    "multiface_corrtalk_realism": 0,
    "multiface_diffspeaker_realism": 0,
    "multiface_talkingstyle_realism": 0,
    "multiface_facediffuser_realism": 0,
    "multiface_gt_realism": 0,
}

multiface_lip_sync = {
    "multiface_voca_lip_sync": 0,
    "multiface_meshtalk_lip_sync": 0,
    "multiface_faceformer_lip_sync": 0,
    "multiface_codetalker_lip_sync": 0,
    "multiface_corrtalk_lip_sync": 0,
    "multiface_diffspeaker_lip_sync": 0,
    "multiface_talkingstyle_lip_sync": 0,
    "multiface_facediffuser_lip_sync": 0,
    "multiface_gt_lip_sync": 0,
}

def main():
    folder_path = r"result/multiface"
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if "multiface" in file_name:
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, "r") as file:
                file_content = file.read()
                digits = [char for char in file_content if char.isdigit()]
                array = [int(digit) for digit in digits]
                
                count(array)
    compution()

def count(array):
    global multiface_face, multiface_lip
    face_indices = [
        [0, 9],
        [1, 10],
        [2, 11],
        [3, 12],
        [4, 13],
        [5, 14],
        [6, 15],
        [7, 16],
        [8, 17],
    ]  
    lip_indices = [
        [18, 27],
        [19, 28],
        [20, 29],
        [21, 30],
        [22, 31],
        [23, 32],
        [24, 33],
        [25, 34],
        [26, 35],
    ]  

    for key, value in multiface_face.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in face_indices[idx]:
                    if element == 1 and "ours" in key:
                        multiface_face[key]+=1
                    if element == 0 and "ours" not in key:
                        multiface_face[key]+=1  

    for key, value in multiface_lip.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in lip_indices[idx]:
                    if element == 1 and "ours" in key:
                        multiface_lip[key]+=1
                    if element == 0 and "ours" not in key:
                        multiface_lip[key]+=1     

def compution():
    global multiface_face, multiface_lip
    global multiface_realism, multiface_lip_sync

    # # 遍历字典的键和值
    # for key, value in multiface_face.items():
    #     print(key, value)

    # for key, value in multiface_lip.items():
    #     print(key, value)

    face_keys = list(multiface_realism.keys())  # 获取字典的所有键并转换为列表
    face_values = list(multiface_face.values())  # 获取字典的所有值并转换为列表
    for i in range(0, len(face_values), 2):
        if i + 1 < len(face_values):  # 检查下一个索引是否存在，确保索引不越界
            multiface_realism[face_keys[int(i/2)]] = round((face_values[i] /(face_values[i] + face_values[i+1]))*100, 2)

    for key, value in multiface_realism.items():
        print(key, value)    
    print('\n')
    lip_keys = list(multiface_lip_sync.keys())  
    lip_values = list(multiface_lip.values())  
    for i in range(0, len(lip_values), 2):
        if i + 1 < len(lip_values):  
            multiface_lip_sync[lip_keys[int(i/2)]] = round((lip_values[i] /(lip_values[i] + lip_values[i+1]))*100, 2)

    for key, value in multiface_lip_sync.items():
        print(key, value)    

    return multiface_realism, multiface_lip_sync

if __name__=='__main__':
    main()

