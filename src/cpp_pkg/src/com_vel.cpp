#include "rclcpp/rclcpp.hpp"
#include "tf2_msgs/msg/tf_message.hpp"
#include "geometry_msgs/msg/twist.hpp"

class CoMVelocityNode : public rclcpp::Node {
public:
    CoMVelocityNode() : Node("com_velocity_from_tf") {
        sub_ = this->create_subscription<tf2_msgs::msg::TFMessage>(
            "/tf", 10,
            std::bind(&CoMVelocityNode::tfCallback, this, std::placeholders::_1)
        );

        pub_ = this->create_publisher<geometry_msgs::msg::Twist>(
            "/com_velocity", 10
        );
    }

private:
    bool first_ = true;
    rclcpp::Time last_time_;
    double last_x_, last_y_;

    void tfCallback(const tf2_msgs::msg::TFMessage::SharedPtr msg) {
        for (const auto &t : msg->transforms) {
            if (t.header.frame_id == "odom" &&
                t.child_frame_id == "base_footprint") {

                double x = t.transform.translation.x;
                double y = t.transform.translation.y;
                rclcpp::Time now = t.header.stamp;

                if (first_) {
                    last_x_ = x;
                    last_y_ = y;
                    last_time_ = now;
                    first_ = false;
                    return;
                }

                double dt = (now - last_time_).seconds();
                if (dt <= 0.0) return;

                geometry_msgs::msg::Twist vel;
                vel.linear.x = (x - last_x_) / dt;
                vel.linear.y = (y - last_y_) / dt;

                pub_->publish(vel);

                last_x_ = x;
                last_y_ = y;
                last_time_ = now;
            }
        }
    }

    rclcpp::Subscription<tf2_msgs::msg::TFMessage>::SharedPtr sub_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CoMVelocityNode>());
    rclcpp::shutdown();
    return 0;
}
