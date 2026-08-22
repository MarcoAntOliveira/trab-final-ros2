cmake_minimum_required(VERSION 3.8)
project(cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
<<<<<<< HEAD
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(proj1_interface REQUIRED)
find_package(rclcpp_action REQUIRED)

# --- Original Executables ---
add_executable(pub_cpp src/pub.cpp)
ament_target_dependencies(pub_cpp rclcpp example_interfaces)

add_executable(test_cpp src/sensor_node.cpp)
ament_target_dependencies(test_cpp rclcpp proj1_interface)

add_executable(sub_cpp src/sub.cpp)
ament_target_dependencies(sub_cpp rclcpp example_interfaces)

add_executable(battery src/battery.cpp)
ament_target_dependencies(battery rclcpp proj1_interface)

add_executable(move_client src/move_robot_client.cpp)
ament_target_dependencies(move_client rclcpp rclcpp_action proj1_interface)

# --- Added Executables (from your error logs) ---
add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_station src/robot_news_station.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)

add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)

add_executable(number_publisher src/number_publisher.cpp)
ament_target_dependencies(number_publisher rclcpp example_interfaces)

add_executable(number_counter src/number_counter.cpp)
ament_target_dependencies(number_counter rclcpp example_interfaces)

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)

add_executable(add_two_ints_client_no_oop src/add_two_ints_client_no_oop.cpp)
ament_target_dependencies(add_two_ints_client_no_oop rclcpp example_interfaces)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

# --- Install Section ---
install(TARGETS
  pub_cpp
  sub_cpp 
  battery
  test_cpp
  move_client
  cpp_node
  robot_news_station
  smartphone
  number_publisher
  number_counter
  add_two_ints_server
  add_two_ints_client_no_oop
  add_two_ints_client
  DESTINATION lib/${PROJECT_NAME}
)
<<<<<<< HEAD
=======

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(tf2_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(interfaces2 REQUIRED)

add_executable(com_vel src/com_vel.cpp)
ament_target_dependencies(com_vel rclcpp tf2_msgs geometry_msgs)

add_executable(tests2 src/sub_test.cpp)
ament_target_dependencies(tests2 rclcpp interfaces2)

install(TARGETS
  com_vel
  tests2
  DESTINATION lib/${PROJECT_NAME}
)

>>>>>>> 1af9a0a (updates)
ament_package()
=======

ament_package()
>>>>>>> 6f382c6 (upload)
