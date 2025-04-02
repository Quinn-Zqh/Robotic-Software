import rclpy
from rclpy.node import Node

class MinorRequirements(Node):
    def __init__(self):
        super().__init__('minor_requirements')
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('MinorRequirements has started.')
    def timer_callback(self):
        self.get_logger().info('grape')

def main(args=None):
    rclpy.init(args=args)
    node = MinorRequirements()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
