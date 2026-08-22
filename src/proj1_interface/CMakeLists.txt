cmake_minimum_required(VERSION 3.8)
project(proj1_interface)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# get all msg files
set(MSGS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/msg")
file(GLOB MSGS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "${MSGS_DIR}/*.msg")

# get all srv files
set(SRVS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/srv")
file(GLOB SRVS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "${SRVS_DIR}/*.srv")

# get all action files
set(ACTIONS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/action")
file(GLOB ACTIONS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "${ACTIONS_DIR}/*.action")

rosidl_generate_interfaces(${PROJECT_NAME}
    ${MSGS}
	${SRVS}
	${ACTIONS}
	DEPENDENCIES builtin_interfaces
	ADD_LINTER_TESTS
 )
 ament_export_dependencies(rosidl_default_runtime)
ament_package()
