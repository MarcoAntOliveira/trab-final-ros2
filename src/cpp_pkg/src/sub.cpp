#include "rclcpp/rclcpp.hpp" 
#include "example_interfaces/msg/int64.hpp"
#include "example_interfaces/srv/set_bool.hpp"

using namespace std::placeholders;
using namespace std::chrono_literals;
class counterNode : public rclcpp::Node 
{
public:
    counterNode() : Node("number_counter") 
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::Int64>("number_publisher", 10, std::bind(&counterNode::callbackNumber, this, std::placeholders::_1 ));
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number_count", 15);
        server_ = this->create_service<example_interfaces::srv::SetBool>("number_count_service",
        std::bind(&counterNode::callNumber, this, _1, _2));
        RCLCPP_INFO(this->get_logger(),"counter has started");

    } 
 


private:
    void callbackNumber(const example_interfaces::msg::Int64::SharedPtr msg){
        
        
        auto msg1 = example_interfaces::msg::Int64();
        msg1.data = msg->data + counter_;
        publisher_->publish(msg1); 
        
    }

       void callNumber(const example_interfaces::srv::SetBool::Request::SharedPtr request, const example_interfaces::srv::SetBool::Response::SharedPtr response){

        if (request->data)
        {
            counter_ = counter_ + 5;
            response->success = true;
            response->message = "Counter added 5+";
        }
        else
        {
            response->success = false;
            response->message = "Nothing added performed";
        }

       
    }



    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Service<example_interfaces::srv::SetBool>::SharedPtr server_;
    int64_t counter_= 5;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<counterNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
