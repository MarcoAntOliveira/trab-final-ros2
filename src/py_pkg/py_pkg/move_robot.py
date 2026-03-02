#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from proj1_interface.action import  RobotSatus
from robot import Robot
import time

class MoveRobotNode(Node): 
    def __init__(self):
        super().__init__("move_robot_server")
        robot = Robot()
        self.atual_position = 0 
        robot.position = self.atual_position
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
        period = 5
        self.get_logger().info("Executing the goal")
        for i in range(target): 
            self.atual_position +=velocity
            self.get_logger().info(str(self.atual_position))
            time.sleep(period)
        goal_handle.succeed()
        result = RobotSatus.Result()
        result.final_position = self.atual_position
        return result 
            
    


def main(args=None):
    rclpy.init(args=args)
    node = MoveRobotNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()