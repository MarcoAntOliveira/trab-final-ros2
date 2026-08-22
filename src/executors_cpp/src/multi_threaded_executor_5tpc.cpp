#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include <chrono>
#include <thread>

using namespace std::chrono_literals;

class Node1 : public rclcpp::Node
{
public:
    Node1() : Node("node1")
    {
        pub1_ = this->create_publisher<example_interfaces::msg::Int64>("topic1", 10);
        pub2_ = this->create_publisher<example_interfaces::msg::Int64>("topic2", 10);
        pub3_ = this->create_publisher<example_interfaces::msg::Int64>("topic3", 10);

        timer1_ = this->create_wall_timer(1000ms, std::bind(&Node1::callbackTimer1, this));
        timer2_ = this->create_wall_timer(1500ms, std::bind(&Node1::callbackTimer2, this));
        timer3_ = this->create_wall_timer(2000ms, std::bind(&Node1::callbackTimer3, this));
    }

private:

    void callbackTimer1()
    {
        std::this_thread::sleep_for(500ms);

        auto msg = example_interfaces::msg::Int64();
        msg.data = count1_++;

        pub1_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing topic1: %ld", msg.data);
    }

    void callbackTimer2()
    {
        std::this_thread::sleep_for(500ms);

        auto msg = example_interfaces::msg::Int64();
        msg.data = count2_++;

        pub2_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing topic2: %ld", msg.data);
    }

    void callbackTimer3()
    {
        std::this_thread::sleep_for(500ms);

        auto msg = example_interfaces::msg::Int64();
        msg.data = count3_++;

        pub3_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing topic3: %ld", msg.data);
    }

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr pub1_, pub2_, pub3_;
    rclcpp::TimerBase::SharedPtr timer1_, timer2_, timer3_;

    int count1_ = 0, count2_ = 0, count3_ = 0;
};

class Node2 : public rclcpp::Node
{
public:
    Node2() : Node("node2")
    {
        pub4_ = this->create_publisher<example_interfaces::msg::Int64>("topic4", 10);
        pub5_ = this->create_publisher<example_interfaces::msg::Int64>("topic5", 10);

        timer4_ = this->create_wall_timer(1200ms, std::bind(&Node2::callbackTimer4, this));
        timer5_ = this->create_wall_timer(1800ms, std::bind(&Node2::callbackTimer5, this));
    }

private:

    void callbackTimer4()
    {
        std::this_thread::sleep_for(500ms);

        auto msg = example_interfaces::msg::Int64();
        msg.data = count4_++;

        pub4_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing topic4: %ld", msg.data);
    }

    void callbackTimer5()
    {
        std::this_thread::sleep_for(500ms);

        auto msg = example_interfaces::msg::Int64();
        msg.data = count5_++;

        pub5_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing topic5: %ld", msg.data);
    }

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr pub4_, pub5_;
    rclcpp::TimerBase::SharedPtr timer4_, timer5_;

    int count4_ = 0, count5_ = 0;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node1 = std::make_shared<Node1>();
    auto node2 = std::make_shared<Node2>();

    // 🔥 ESSENCIAL: usar MultiThreadedExecutor
    rclcpp::executors::MultiThreadedExecutor executor;
    executor.add_node(node1);
    executor.add_node(node2);

    executor.spin();

    rclcpp::shutdown();
    return 0;
}