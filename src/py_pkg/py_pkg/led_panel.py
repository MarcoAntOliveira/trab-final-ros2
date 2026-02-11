#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from proj1_interface.msg import StatePanel
from proj1_interface.srv import SetLed


class LedPanelNode(Node): 
    def __init__(self):
        super().__init__("led_panel_state") 
        self.led_publisher_ = self.create_publisher(
            StatePanel, "led_panel_state", 10)
        self.led_server_=self.create_service(SetLed,"set_led",)
        
    def callback_led(self, request:SetLed.Request , response:SetLed.Response):
        msg1 = StatePanel()
        if(request ==True):
            msg1.led[1] = 1 
            self.led_publisher_.publish(msg1)
            response = "y"
        else:
            msg1.led[1] = 0
            self.led_publisher_.publish(msg1)
            response = "y"


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()