# trab-final-ros2

## ROS 2 – Publisher & Subscriber Exercise

You’ll create **2 nodes from scratch**.

-   In the first one, you’ll have **1 publisher**
-   In the second one, **1 publisher & 1 subscriber**

---

### Nodes Description

#### `number_publisher`

-   Publishes a number (always the same) on the **`/number`** topic
-   Uses existing message type:  
    `example_interfaces/msg/Int64`

#### `number_counter`

-   Subscribes to the **`/number`** topic
-   Keeps a **counter variable**
-   Every time a new number is received, it is **added to the counter**
-   Has a publisher on the **`/number_count`** topic
-   When the counter is updated, the new value is **published immediately**

---

### Hints

-   Check what is inside `example_interfaces/msg/Int64` using the command line tool:
    
    ```bash
    ros2 interface show example_interfaces/msg/Int64
    ```

# ROS 2 – Services

## Architecture Overview

number_publisher --> /number --> number_counter --> /number_count
|
+--> /reset_counter (service)

- `/number`  
  Message type: `example_interfaces/msg/Int64`

- `/number_count`  
  Message type: `example_interfaces/msg/Int64`

- `/reset_counter`  
  Service type: `example_interfaces/srv/SetBool`

---

## Reset Counter Functionality

Add a functionality to **reset the counter to zero**.

### Requirements

- Create a **service server** inside the `number_counter` node.
- Service name:  
/reset_counter
- Service type:  

> Use the following command to inspect the service interface:
```bash
ros2 interface show example_interfaces/srv/SetBool
