import rclpy
from rclpy.node import Node
import time


class MyTimer(Node):
    def __init__(self):
        super().__init__('time_printer')
        self.timer = self.create_timer(5.0, self.timer_callback)

    def timer_callback(self):
        cur_time = time.strftime("%H:%M:%S", time.localtime())
        self.get_logger().info(cur_time)


def main(args=None):
    rclpy.init(args=args)

    node = MyTimer()

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
