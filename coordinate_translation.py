import os
import open3d as o3d

# 指定输入文件夹和输出文件夹
input_folder = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_translate\\objects"
output_folder = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_translate\\correct_position"

# 获取输入文件夹中的所有文件名
file_names = os.listdir(input_folder)

# 遍历文件夹中的每个文件
for file_name in file_names:
    # 构建输入文件的完整路径
    input_file = os.path.join(input_folder, file_name)
    
    # 读取点云文件
    point_cloud = o3d.io.read_point_cloud(input_file)
    
    # 平移
    point_cloud.translate((177071.5847, 2535992.64, 46.2339),relative=True)
    
    # 构建输出文件的完整路径
    output_file = os.path.join(output_folder, file_name)
    
    # 保存处理后的点云
    o3d.io.write_point_cloud(output_file, point_cloud)
