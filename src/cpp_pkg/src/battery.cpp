#include "rclcpp/rclcpp.hpp"
#include "proj1_interface/msg/state.hpp"
#include "proj1_interface/srv/set_led.hpp"

using namespace std::chrono_literals;
using namespace std::placeholders;

class BatteryNode : public rclcpp::Node 
{
public:
    BatteryNode() : Node("battery_state") 
    {   
        publisher_ =
            this->create_publisher<proj1_interface::msg::State>(
                "battery_state", 15);
        client_ = this->create_client<proj1_interface::srv::SetLed>(
            "set_led"
        );
       
        request_ =
                  std::make_shared<proj1_interface::srv::SetLed::Request>();


        timerFull_ = this->create_wall_timer(
            6s,
            std::bind(&BatteryNode::batteryFull, this));

        timerEmpty_ = this->create_wall_timer(
            4s,
            std::bind(&BatteryNode::batteryEmpty, this));
    }

private:
    proj1_interface::msg::State msg;
       void batteryFull()
{
    msg.state = "full";
    publisher_->publish(msg);

    request_->turn = false;

    client_->async_send_request(
        request_,
        std::bind(&BatteryNode::callbackBattery, this, std::placeholders::_1)
    );
}

void batteryEmpty()
{
    msg.state = "empty";
    publisher_->publish(msg);

    request_->turn = true;

    client_->async_send_request(
        request_,
        std::bind(&BatteryNode::callbackBattery, this, std::placeholders::_1)
    );
}

    void callbackBattery(rclcpp::Client<proj1_interface::srv::SetLed>::SharedFuture future){
        auto response = future.get();
        RCLCPP_INFO(
            this->get_logger(),
            "res %c",
            static_cast<char>(response->feedback)
);

    }
    rclcpp::Publisher<proj1_interface::msg::State>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timerFull_;
    rclcpp::TimerBase::SharedPtr timerEmpty_;
    proj1_interface::srv::SetLed::Request::SharedPtr request_;
    rclcpp::Client<proj1_interface::srv::SetLed>::SharedPtr client_;

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<BatteryNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}