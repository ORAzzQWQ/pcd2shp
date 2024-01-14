import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
import geopandas as gpd
from shapely.geometry import Polygon
from concave_hull import concave_hull, concave_hull_indexes
import os

#選擇經分類好的pcd資料夾
# 文件夹路径
input_folder_path = "C:\\Users\\annie\\Desktop\\測量專題\\pcd_classify\\AMG\\AMG_Right Arrow"
output_folder_path = "C:\\Users\\annie\\Desktop\\測量專題\\pcd2shp_concave\\SHP_AMG_Right Arrow"
file_names = [f for f in os.listdir(input_folder_path) if f.endswith('.pcd')]
id = 1

# 读取点云数据并转换为NumPy数组
for target_pointcould in file_names:
    file_path = os.path.join(input_folder_path, target_pointcould)

    # 读取PCD文件
    point_cloud = o3d.io.read_point_cloud(file_path)
    points = np.asarray(point_cloud.points)
    print(points)

    # 凹多边形的边界点
    threshold = 0.3
    idxes = concave_hull_indexes(
        points[:, :2],
        concavity = threshold,
        length_threshold = threshold,
    )

    # 验证凹多边形的索引点
    assert np.all(points[idxes] == concave_hull(points, concavity = threshold, length_threshold = threshold))

    #凹多邊形的邊界線
    concave_seg_points = []
    concave_seg_points = [points[[f, t]] for f, t in zip(idxes[:-1], idxes[1:])]

    # 确保端点形成闭合轮廓，即第一个点和最后一个点相同
    if not np.array_equal(concave_seg_points[0][0], concave_seg_points[-1][-1]):
        concave_seg_points.append(concave_seg_points[0][0])

    # 转换成array，连成polygon
    concave_seg_points = np.vstack(concave_seg_points)
    polygon_3d = Polygon(concave_seg_points)
    data = {'id': [1], 'geometry': [polygon_3d]}
    gdf = gpd.GeoDataFrame(data, crs="EPSG:3826")  # 使用 TWD97 的坐标参考系统

    # 導出為 Shapefile
    os.makedirs(output_folder_path, exist_ok=True)
    export_path = f"{output_folder_path}\\{id:06d}.shp"
    gdf.to_file(export_path, driver='ESRI Shapefile')
    
    id += 1