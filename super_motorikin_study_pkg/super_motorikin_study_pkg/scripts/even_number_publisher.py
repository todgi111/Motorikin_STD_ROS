#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__('None')
        
        self.declare_parameter('mode', 'None')
        self.declare_parameter('publish_frequency', 10.0)
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_name', 'even_numbers')
        self.declare_parameter('overflow_topic_name', 'overflow')
        
        self.mode = self.get_parameter('mode').value
        
        if self.mode == 'fast':
            self.freq = 20
            self.threshold = 50
            self.topic = 'even_numbers_fast'
        elif self.mode == 'slow':
            self.freq = 5
            self.threshold = 150
            self.topic = 'even_numbers_slow'
        else:
            self.freq = self.get_parameter('publish_frequency').value
            self.threshold = self.get_parameter('overflow_threshold').value
            self.topic = self.get_parameter('topic_name').value
            
        self.overflow_topic = self.get_parameter('overflow_topic_name').value

        self.publisher = self.create_publisher(Int32, self.topic, 10)
        self.overflow_pub = self.create_publisher(Int32, self.overflow_topic, 10)
        self.counter = 0

        self.timer = self.create_timer(1/self.freq, self.timer_callback)
        
    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        
        if self.counter >= self.threshold:
            self.overflow_pub.publish(msg)
            self.get_logger().info(f'Printed in {self.overflow_topic}: {msg.data}')
            self.counter = 0
        else:
            self.publisher.publish(msg)
            self.get_logger().info(f'Printed in {self.topic}: {msg.data}')
            
            self.counter += 2

def main():
    rclpy.init()

    node = Talker()
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

