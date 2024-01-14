import os
import numpy as np
import struct
import csv

folder = "c:\\Users\\annie\\Desktop\\pcdTEST"

#pcd_folder = 'C:\\Users\\Point\\Desktop\\OpenDRIVE_auto\\AMG_Double White Line'
#csv_folder = 'C:\\Users\\Point\\Desktop\\OpenDRIVE_auto\\vscode'

def pcd2csv(file_path):
    with open(file_path, "rb") as f:
        # 跳過 PCD 文件头

        line = f.readline().rstrip()
        while not line.startswith(b"POINTS"):
            line = f.readline().rstrip()
        num_points = int(line.split(b" ")[1])

        while True:
            line = f.readline().strip()
            if line == b"DATA binary":
                break
        
        # 將 PCD 文件轉換為 CSV 文件
        csv_file = os.path.splitext(file_path)[0] + ".csv"
        with open(csv_file, "w") as fw:
            # fw.write("x,y,z\n")
            for i in range(num_points):
                data = f.read(16)
                x, y, z ,rgb = struct.unpack("fffI", data)
                fw.write(f"{x},{y},{z}\n")

# 將 PCD 文件夾中的所有文件轉換為 CSV 文件
pcd_dir = folder
for filename in os.listdir(pcd_dir):
    if filename.endswith(".pcd"):
        file_path = os.path.join(pcd_dir, filename)
        pcd2csv(file_path)