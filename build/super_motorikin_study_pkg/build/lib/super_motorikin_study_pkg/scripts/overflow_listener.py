#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int32

class Listener(Node):

    def __init__(self):
        super().__init__('None')
        
        self.declare_parameter('overflow_topic_name', 'overflow')
        self.overflow_topic = self.get_parameter('overflow_topic_name').value

        self.subscription = self.create_subscription(Int32, self.overflow_topic, self.callback, 10)

    def callback(self, msg):
        self.get_logger().warn(f"!!! ПЕРЕПОЛНЕНИЕ !!! В топик {self.overflow_topic} получено значение: {msg.data}")

def main():
    rclpy.init() 
    
    node = Listener() 
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass                      
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
