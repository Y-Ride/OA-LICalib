import open3d as o3d

# Load the PCD file
pcd = o3d.io.read_point_cloud("results/imu_calibration_ros1/refined_map-iter13-seg0.pcd")

# Visualize
o3d.visualization.draw_geometries([pcd])
