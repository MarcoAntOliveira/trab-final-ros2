import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading

class CmdVelPlotter(Node):
    def __init__(self):
        super().__init__('cmd_vel_plotter')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )

        # Buffer circular (últimos 100 pontos)
        self.data = deque(maxlen=100)

    def listener_callback(self, msg):
        self.data.append(msg.linear.x)


def ros_spin(node):
    rclpy.spin(node)


def main():
    rclpy.init()

    node = CmdVelPlotter()

    # Thread ROS (para não travar o matplotlib)
    thread = threading.Thread(target=ros_spin, args=(node,))
    thread.start()

    # Matplotlib
    fig, ax = plt.subplots()
    ax.set_title("cmd_vel.linear.x (tempo real)")
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Velocidade linear X")

    line, = ax.plot([], [], lw=2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(0, 100)

    def update(frame):
        y = list(node.data)
        x = list(range(len(y)))
        line.set_data(x, y)
        return line,

    ani = animation.FuncAnimation(
        fig,
        update,
        interval=100,
        blit=True
    )

    plt.show()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
