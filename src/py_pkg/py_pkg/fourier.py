import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import numpy as np


class FourierCompare(Node):

    def __init__(self):
        super().__init__('fourier_compare')

        self.pub_original = self.create_publisher(Float64, 'signal_original', 10)
        self.pub_phase = self.create_publisher(Float64, 'signal_phase', 10)

        self.timer = self.create_timer(0.01, self.update)

        self.t = 0.0
        self.dt = 0.01

        self.Im = 1.0
        self.w = 2*np.pi
        self.phi = np.pi/4

        self.N = 10  # número de harmônicos

    def series_original(self, t):
        s = 0.0
        for n in range(1, self.N+1):
            s += np.sin(n*self.w*t - self.phi)
        return s

    def series_phase(self, t):
        s = 0.0
        for n in range(1, self.N+1):
            s += np.sin(n*self.w*t - n*self.phi)
        return s

    def update(self):

        y1 = self.series_original(self.t)
        y2 = self.series_phase(self.t)

        msg1 = Float64()
        msg2 = Float64()

        msg1.data = y1
        msg2.data = y2

        self.pub_original.publish(msg1)
        self.pub_phase.publish(msg2)

        self.t += self.dt


def main():
    rclpy.init()
    node = FourierCompare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()