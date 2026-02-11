#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include "example_interfaces/srv/set_bool.hpp"

using namespace std::chrono_literals;

class NumberPublisherNode : public rclcpp::Node
{
public:
    NumberPublisherNode() : Node("number_publisher_node"), counter_(15)
    {
        publisher_ =
            this->create_publisher<example_interfaces::msg::Int64>(
                "number_publisher", 15);

        timer_ = this->create_wall_timer(
            0.5s,
            std::bind(&NumberPublisherNode::numberCallback, this));

        server_ = this->create_service<example_interfaces::srv::SetBool>(
            "reset_counter",
            std::bind(
                &NumberPublisherNode::resetCallback,
                this,
                std::placeholders::_1,
                std::placeholders::_2));

        RCLCPP_INFO(this->get_logger(), "Node started");
    }

private:
    // 🔁 TIMER CALLBACK → sem argumentos
    void numberCallback()
    {
        example_interfaces::msg::Int64 msg;
        msg.data = counter_;
        publisher_->publish(msg);
    }

   
    void resetCallback(
        const example_interfaces::srv::SetBool::Request::SharedPtr request,
        example_interfaces::srv::SetBool::Response::SharedPtr response)
    {
        if (request->data)
        {
            counter_ = 0;
            response->success = true;
            response->message = "Counter reset";
        }
        else
        {
            response->success = false;
            response->message = "No reset performed";
        }
    }

    int64_t counter_;

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Service<example_interfaces::srv::SetBool>::SharedPtr server_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<NumberPublisherNode>());
    rclcpp::shutdown();
    return 0;
}
