import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mscrobotics2425laptop17/ros2_tutorial_workspace/src/mitsubishi/install/mitsubishi'
