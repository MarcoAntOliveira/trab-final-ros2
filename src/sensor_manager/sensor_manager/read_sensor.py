import rclpy
from rclpy.node import Node

import serial
from example_interfaces.msg import Float32

class SerialSensorNode(Node):
    def __init__(self):
        super().__init__('serial_sensor_node')

        self.pubx = self.create_publisher(Float32, 'sensor/linear/x', 10)
        self.puby = self.create_publisher(Float32, 'sensor/linear/y', 10)
        self.pubz = self.create_publisher(Float32, 'sensor/linear/z', 10)

        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=115200,
            timeout=0.1
        )

        self.timer = self.create_timer(0.02, self.read_serial)

    def read_serial(self):
        try:
           
            raw = self.ser.readline()

            

            if not raw:
                self.get_logger().info("STEP 3: raw vazio (timeout)")
                return

            line = raw.decode('utf-8', errors='ignore').strip()
    

            parts = line.split()
         
            valuex = parts[0].strip()  # remove \n, \r, espaços
            valuey = parts[1].strip()  # remove \n, \r, espaços
            valuez = parts[2].strip()  # remove \n, \r,
            try:
                valuex_f = float(valuex)
                valuey_f = float(valuey)
                valuez_f = float(valuez)
            except ValueError as e:
                self.get_logger().error(f"Erro no cast: valuex='{valuex}', valuey='{valuey}', valuez='{valuez}' ({e})")
                return
            msgx = Float32()
            msgy = Float32()
            msgz = Float32()
            msgx.data = valuex_f
            msgy.data = valuey_f
            msgz.data = valuez_f
            self.pubx.publish(msgx)
            self.puby.publish(msgy)
            self.pubz.publish(msgz)
            self.get_logger().info("STEP 7: published")

        except Exception as e:
            self.get_logger().error(f"ERROR: {e}")

def main(args=None): 
    rclpy.init(args=args) 
    node = SerialSensorNode() 
    rclpy.spin(node) 
    node.destroy_node() 
    rclpy.shutdown() 
    
if __name__ == '__main__': 
    main()