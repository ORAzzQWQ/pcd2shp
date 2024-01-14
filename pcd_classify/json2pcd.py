import json
import os
import shutil


# Parameters 輸入端點坐標
source_folder = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_translate\\objects"
target_folder = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_classify\\AMG\\"

# 讀取 JSON 文件
with open("C:\\Users\\annie\\Desktop\\測量專題\\pcd_classify\\pc_dataset_amg_format.json" , 'r') as file:
    data = json.load(file)


def classify(item, category_name):
    # 輸出對應的 "object_file"   提取最後的10個字元
    file_name = item["object_file"][-10:]
        
    # 搜尋資料夾中相同名稱的檔案
    for filename in os.listdir(source_folder):
        if filename.endswith(file_name):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder+category_name, filename)
            shutil.copy2(source_path, target_path)
    return 0


# 循環遍歷每個數據元素
for item in data["annotations"]:
    if "category_id" in item and item["category_id"] == "0":
        classify(item, "AMG_VOID")
    elif "category_id" in item and item["category_id"] == "1":
        classify(item, "AMG_Text")
    elif "category_id" in item and item["category_id"] == "2":
        classify(item, "AMG_General Marking")
    elif "category_id" in item and item["category_id"] == "3":
        classify(item, "AMG_Driving Area")   
    elif "category_id" in item and item["category_id"] == "4":
        classify(item, "AMG_Curb")
    elif "category_id" in item and item["category_id"] == "5":
        classify(item, "AMG_Stop Line")
    elif "category_id" in item and item["category_id"] == "6":
        classify(item, "AMG_White Line")
    elif "category_id" in item and item["category_id"] == "7":
        classify(item, "AMG_Double White Line")
    elif "category_id" in item and item["category_id"] == "8":
        classify(item, "AMG_Yellow Line")
    elif "category_id" in item and item["category_id"] == "9":
        classify(item, "AMG_Double Yellow Line") 
    elif "category_id" in item and item["category_id"] == "10":
        classify(item, "AMG_Crossing Line")
    elif "category_id" in item and item["category_id"] == "11":
        classify(item, "AMG_Crossing")
    elif "category_id" in item and item["category_id"] == "12":
        classify(item, "AMG_Forward Arrow")
    elif "category_id" in item and item["category_id"] == "13":
        classify(item, "AMG_Left Arrow")
    elif "category_id" in item and item["category_id"] == "14":
        classify(item, "AMG_Right Arrow")
    elif "category_id" in item and item["category_id"] == "15":
        classify(item, "AMG_Pole")
    elif "category_id" in item and item["category_id"] == "16":
        classify(item, "AMG_Traffic Light")
    elif "category_id" in item and item["category_id"] == "17":
        classify(item, "AMG_Crossing Light")
    elif "category_id" in item and item["category_id"] == "18":
        classify(item, "AMG_Stop Sign")
    elif "category_id" in item and item["category_id"] == "19":
        classify(item, "AMG_Traffic Sign")        

