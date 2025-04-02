import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger
import time

class Date(Node):
    def __init__(self):
        super().__init__('date')
        self.client = self.create_client(Trigger, 'fix')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service to become available...')
        
        self.call_service()

    def call_service(self):
        req = Trigger.Request()
        self.future = self.client.call_async(req)
        self.future.add_done_callback(self.handle_response)

    def handle_response(self, future):
        response = future.result()
        if response:
            self.get_logger().info(f'Service response: {response.message}')
            # 以 2 Hz 打印 message 字段
            self.timer = self.create_timer(0.5, self.print_message)
            self.message = response.message

    def print_message(self):
        self.get_logger().info(f'{self.message}')

def main(args=None):
    rclpy.init(args=args)
    node = Date()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

