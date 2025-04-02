import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Projector(Node):
    def __init__(self):
        super().__init__('projector')
        self.subscription = self.create_subscription(
            String,
            'replace',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Projector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

