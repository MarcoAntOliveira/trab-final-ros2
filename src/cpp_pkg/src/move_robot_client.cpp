#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "proj1_interface/action/robot_status.hpp"

using RobotStatus = proj1_interface::action::RobotStatus;
class MoveRobotClientNode : public rclcpp::Node 
{
public:
    MoveRobotClientNode() : Node("node_name") 
    {
        move_robot_client_ = rclcpp_action::create_client<RobotStatus>(this, "move_robot");
    }

    void send_goal(int final_position, int velocity){


    }

private:
    rclcpp_action::Client<RobotStatus>::SharedPtr move_robot_client_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MoveRobotClientNode>(); 
    node->send_goal(6,0.5);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
