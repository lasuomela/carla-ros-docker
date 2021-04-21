
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

import os

def generate_launch_description():
    return LaunchDescription([
    	IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('carla_ros_bridge'), 'carla_ros_bridge.launch.py')
            ),
            launch_arguments={
                'world': 'PATH',
                'verbose': 'true'
            }.items()
    	),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('carla_spawn_objects'), 'carla_example_ego_vehicle.launch.py')
            ),
            launch_arguments={
                'world': 'PATH',
                'verbose': 'true'
            }.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('carla_waypoint_publisher'), 'carla_waypoint_publisher.launch.py')
            ),
            launch_arguments={
                'world': 'PATH',
                'verbose': 'true'
            }.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('carla_ad_agent'), 'carla_ad_agent.launch.py')
            ),
            launch_arguments={
                'world': 'PATH',
                'verbose': 'true',
                'avoid_risk': 'false'
            }.items()
        ),
         Node(
            package='rviz2',
            namespace='rviz2',
            executable='rviz2',
            name='rviz2',
            output="screen",
        ),
    ])

