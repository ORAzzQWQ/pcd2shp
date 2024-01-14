import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
from scipy.spatial import ConvexHull
import geopandas as gpd
from shapely.geometry import Polygon
import os

# pip install -U concave_hull
from concave_hull import concave_hull, concave_hull_indexes

#選擇經分類好的pcd資料夾
# 文件夹路径
input_folder_path = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_classify\\AMG\\AMG_Crossing"
output_folder_path = "C:\\Users\\annie\\Desktop\\測量專題\\pcd2shp_convex\\SHP_AMG_Crossing"
file_names = [f for f in os.listdir(input_folder_path) if f.endswith('.pcd')]

id = 0 #shp id

# 读取点云数据并转换为NumPy数组
for target_pointcould in file_names:
    
    file_path = os.path.join(input_folder_path, target_pointcould)

    # 读取PCD文件
    point_cloud = o3d.io.read_point_cloud(file_path)

    points = np.asarray(point_cloud.points)
    convex_hull = ConvexHull(points[:, :2])

    #凸包
    vertices = points[convex_hull.vertices]
    print(vertices)

    # 確保端點形成閉合輪廓，即第一個點和最後一個點相同
    if (vertices[0], vertices[-1]) == False:
        vertices.append(vertices[0])

    #轉換成array，連成polygon
    polygon_3d = Polygon(vertices)
    data = {'id': [id], 'geometry': [polygon_3d]}
    gdf = gpd.GeoDataFrame(data, crs="EPSG:3826")  # 使用 TWD97 的坐標參考系統

    # 導出為 Shapefile
    os.makedirs(output_folder_path, exist_ok=True)

    export_path = f"{output_folder_path}\\{id:06d}.shp"
    gdf.to_file(export_path, driver='ESRI Shapefile')

    id += 1