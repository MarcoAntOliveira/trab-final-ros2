# Use bash em vez do sh padrãoc
SHELL := /bin/bash
all: launch
sensor: sensor_manager publisher_sensor
pub: pub_cpp pub_py
up: 
	@echo "Atualizando workspace..."
	source install/setup.bash
	source /opt/ros/$(ROS_DISTRO)/setup.bash
	source /home/marco/projects/proj1/install/setup.bash
	

bil:

	@echo "Atualizando workspace..."
	cd ~/projects/proj1/ 
	colcon build
	source install/setup.bash
	source /opt/ros/$(ROS_DISTRO)/setup.bash
launch: 
	@echo "Lançando Gazebo..."
	source install/setup.bash && ros2 launch my_robot_bringup my_robot_gazebo.launch.xml

move:
	@echo "Abrindo Teleop em uma janela xterm independente..."
	xterm -e "bash -c 'source /opt/ros/$(ROS_DISTRO)/setup.bash; source install/setup.bash; ros2 run teleop_twist_keyboard teleop_twist_keyboard; exec bash'" &

plot:
	@echo "Iniciando gráfico e enviando comando de movimento..."
	# Abre o gráfico em uma janela separada e continua a execução
	xterm -e "bash -c 'python3 plot_cmd_vel.py'" & 
	# Aguarda 2 segundos para o gráfico carregar antes de publicar
	sleep 2
	# Publica o movimento (source necessário para reconhecer o tipo da mensagem)
	source /opt/ros/jazzy/setup.bash && ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.0}}"

go:
	cd src/my_robot_plot_topic/my_robot_plot_topic 
sensor_manager:
	colcon build --packages-select sensor_manager --symlink-install
	source install/setup.bash


publisher_sensor:
	source install/setup.bash && ros2 run sensor_manager read_sensor

publisher:
	source install/setup.bash && ros2 run py_pkg pub
bil_py:
	colcon build --packages-select py_pkg --symlink-install
	source install/setup.bash
bil_cpp:
	colcon build --packages-select cpp_pkg --symlink-install
	source install/setup.bash
bil_interfaces:
	colcon build --packages-select proj1_interface --symlink-install
	source install/setup.bash
pub_cpp:
	source /opt/ros/jazzy/setup.bash &
	source install/setup.bash &
	ros2 run cpp_pkg pub_cpp & 
	xterm -e "bash -c 'ros2 run cpp_pkg sub_cpp'" & 

pub_py:
	xterm -e "bash -c 'source /opt/ros/jazzy/setup.bash; source install/setup.bash; ros2 run py_pkg pub'"


count_py:
	source install/setup.bash && ros2 run py_pkg pub

test_py:
	source install/setup.bash && ros2 run py_pkg test

test_cpp:
	
	source install/setup.bash && ros2 run cpp_pkg test_cpp

service_pub:
	source /home/marco/projects/proj1/install/setup.bash
	ros2 service call /number_count_service example_interfaces/srv/SetBool "{data: true}"
service_pub2:
	source /home/marco/projects/proj1/install/setup.bash
	ros2 service call /reset_counter example_interfaces/srv/SetBool "{data: true}"


control:
	source install/setup.bash && ros2 run joy joy_node
	ros2 topic echo /joy

control2:
	source install/setup.bash && ros2 run teleop_twist_joy teleop_node \
  --ros-args --params-file ps4.yaml
	ros2 topic echo /cmd_vel
turtle:
	source /opt/ros/$(ROS_DISTRO)/setup.bash
	ros2 run turtlesim turtlesim_node -ros-args -r __node:=my_turtle
turtle_control:
	ros2 run turtlesim turtle_teleop_key
