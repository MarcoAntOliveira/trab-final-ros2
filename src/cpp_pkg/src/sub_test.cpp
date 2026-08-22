#include "rclcpp/rclcpp.hpp"
#include "interfaces2/msg/data_int.hpp"

class Reader : public rclcpp::Node
{
public:
    Reader() : Node("reader")
    {
        sub_ = this->create_subscription<interfaces2::msg::DataInt>(
            "sensor/temp", 10,
            std::bind(&Reader::callback, this, std::placeholders::_1));
    }

private:
    void callback(const interfaces2::msg::DataInt::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Temp=%.2f ",
                    msg->dados);
    }

    rclcpp::Subscription<interfaces2::msg::DataInt>::SharedPtr sub_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Reader>());
    rclcpp::shutdown();
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       