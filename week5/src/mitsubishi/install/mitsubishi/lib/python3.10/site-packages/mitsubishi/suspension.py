import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class NodeA(Node):
    def __init__(self):
        super().__init__('node_a')
        self.srv = self.create_service(Trigger, 'service', self.handle_service)
        self.get_logger().info('Service "service" is ready')

    def handle_service(self, request, response):
        response.success = True
        response.message = 'text'  # 设置 message 为 "text"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = NodeA()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

