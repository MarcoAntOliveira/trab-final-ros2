#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class EkfNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_ = 0
        self.ekf_pub_ = self.create_publisher(
            Int64, "ekf_publisher", 10)
        self.number_subscriber_ = self.create_subscription(
            Int64, "sensor/linear/x", self.callback_ekf, 15)
        self.get_logger().info("Number Counter has been started.")

    def callback_ekf(self, msg: Int64):
        
        msg1 = Int64()
        msg1.data = msg.data + 10
        self.ekf_pub_.publish(msg1)


def main(args=None):
    rclpy.init(args=args)
    node = EkfNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()