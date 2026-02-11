#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from proj1_interface.action import  RobotSatus
import time

class MoveRobotNode(Node): 
    def __init__(self):
        super().__init__("move_robot_server")
        self.atual_position = 0 
        self.move_robot_server = ActionServer(
            self,
            RobotSatus,
            "move_robot",
            execute_callback=self.execute_callback
            )
        self.get_logger().info("Action server has been started")
    def execute_callback(self, goal_handle:ServerGoalHandle):
        target = goal_handle.request.position
        velocity = goal_handle.request.velocity

        self.get_logger().info("Executing the goal")
        for i in range(target): 
            self.atual_position += velocity
            if(self.atual_position == target):
                break
    


def main(args=None):
    rclpy.init(args=args)
    node = MoveRobotNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()