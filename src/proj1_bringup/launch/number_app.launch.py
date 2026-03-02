from launch import LaunchDescription
from launch_ros.actions import Node 
from ament_index_python.packages import get_package_share_directory
import os

param_config =os.path.join(get_package_share_directory("proj1_bringup"),
                           "config","number_app.yaml")

def generate_launch_description():
    ld= LaunchDescription()
    number_pub = Node(
        package="py_pkg",
        executable="pub",
        name="my_number_pubisher",
        remappings=[("/number_count2", "/my_number")],
        parameters=[param_config]
    )

    number_counter=Node(
        package="cpp_pkg",
        executable = "pub_cpp",
        name="my_number_cunter",
        remappings=[("/number_publisher", "/my_pub")]   
    )
    ld.add_action(number_pub)
    ld.add_action(number_counter) 
    return ld

        
