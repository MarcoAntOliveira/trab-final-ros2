#include "rclcpp/rclcpp.hpp"
#include "proj1_interface/msg/data_int.hpp"

using namespace std::chrono_literals;

class SensorNode : public rclcpp::Node
{
public:
    SensorNode() : Node("sensor_node")
    {
        publisher_ = this->create_publisher<proj1_interface::msg::DataInt>("sensor/temp", 10);
        timer_ = this->create_wall_timer(1s, std::bind(&SensorNode::timer_callback, this));
    }

private:
    void timer_callback()
    {
        auto msg = proj1_interface::msg::DataInt();
        msg.dados = 25.5; // aqui você lê o sensor real
        RCLCPP_INFO(this->get_logger(), "Publishing: %.2f", msg.dados);
        publisher_->publish(msg);
    }

    rclcpp::Publisher<proj1_interface::msg::DataInt>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SensorNode>());
    rclcpp::shutdown();
    return 0;
}
