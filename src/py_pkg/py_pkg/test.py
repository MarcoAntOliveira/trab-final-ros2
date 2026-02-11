import rclpy
from std_msgs.msg import Float32

def main():
    rclpy.init()
    node = rclpy.create_node('sensor_node')
    pub = node.create_publisher(Float32, 'sensor/temp', 10)

    while rclpy.ok():
        msg = Float32()
        msg.data = 11.0
        pub.publish(msg)
