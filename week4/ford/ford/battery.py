import rclpy
from rclpy.node import Node
from example_interfaces.msg import UInt32

class Battery(Node):
    def __init__(self):
        super().__init__('battery')
        self.publisher_ = self.create_publisher(UInt32, 'replace', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        msg = UInt32()
        msg.data = "316"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Battery()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

