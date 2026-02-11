#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_ = 0
        self.number_count_publisher_ = self.create_publisher(
            Int64, "number_count2", 10)
        self.number_subscriber_ = self.create_subscription(
            Int64, "number_publisher", self.callback_number, 15)
        self.get_logger().info("Number Counter has been started.")

    def callback_number(self, msg: Int64):
        
        msg1 = Int64()
        msg1.data = msg.data + 10
        self.number_count_publisher_.publish(msg1)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()