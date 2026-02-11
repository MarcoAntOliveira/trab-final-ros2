cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(proj1_interface REQUIRED)


add_executable(pub_cpp src/pub.cpp)
ament_target_dependencies(pub_cpp rclcpp example_interfaces)

add_executable(test_cpp src/sensor_node.cpp)
ament_target_dependencies(test_cpp rclcpp proj1_interface)

add_executable(sub_cpp src/sub.cpp)
ament_target_dependencies(sub_cpp rclcpp example_interfaces)

add_executable(battery src/battery.cpp)
ament_target_dependencies(battery rclcpp proj1_interface)

add_executable(move_client src/move_robot_client.cpp)
ament_target_dependencies(move_client rclcpp proj1_interface)


install(TARGETS
  pub_cpp
  sub_cpp 
  battery
  test_cpp
  move_client
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
