
import launch
from launch import LaunchDescription
from launch.actions import Shutdown
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

import os

package_name = "place_reg_ad"
rviz2_config_path = "config/carla_goal_pose_demo_ros2.rviz"
objects_config_path = os.path.join(get_package_share_directory(package_name), "config/objects.json")


def generate_launch_description():
    ld = LaunchDescription([
    	launch.actions.DeclareLaunchArgument(
            name='role_name',
            default_value='ego_vehicle'
        ),
        launch.actions.DeclareLaunchArgument(
            name='objects_config',
            default_value=objects_config_path
        ),
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
                'objects_definition_file': launch.substitutions.LaunchConfiguration('objects_config'),
                'role_name': launch.substitutions.LaunchConfiguration('role_name')
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
            executable='rviz2',
            name='rviz2',
            output='screen',
 	    remappings=[
                (
                    "carla/ego_vehicle/spectator_pose",
                    "/carla/ego_vehicle/rgb_view/control/set_transform"
                )
                ],
            arguments=[
                '-d', os.path.join(get_package_share_directory(package_name), rviz2_config_path)],
            on_exit=Shutdown()
        ),
    ])
    return ld
    
    

if __name__ == '__main__':
    generate_launch_description()
