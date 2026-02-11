 value="$(find-pkg-share my_robot_description)/urdf/standalone_arm.urdf.xacro"/>
 ros2 pkg create py_pkg --build-type ament_python --dependencies rclpy 

 ros2 pkg create cpp_pkg --build-type ament_cmake --dependencies rclcpp