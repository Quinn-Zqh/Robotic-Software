from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_saver_server',
            name='map_saver_server',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'save_map_timeout': 1000.0,
                'free_thresh': 0.25,
                'occupied_thresh': 0.65,
            }]
        )
    ])

