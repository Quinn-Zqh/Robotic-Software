from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='package_c',  # 您的节点所在的包
            executable='node_c',  # 要启动的节点名称
            name='node_c',  # 节点的名称
            parameters=[
                {'parameter_string': 'acidity'},  # 设置参数 'parameter_string' 的值为 'parameter_a'
                {'parameter_float': '124.0'},   # 设置参数 'parameter_float' 的值为 'parameter_b'
            ]
        )
    ])

