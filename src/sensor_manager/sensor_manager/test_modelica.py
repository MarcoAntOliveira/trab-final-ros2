#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import fmpy
from fmpy import instantiate_fmu

# Caminho do seu FMU
fmu_path = '/tmp/OpenModelica_marco/OMEdit/test_rs.fmu'

class FMUControllerNode(Node):
    def __init__(self):
        super().__init__("FMUController")
        
        self.pub_out = self.create_publisher(Int64, 'fmu_output', 10)
        self.sub_in = self.create_subscription(Int64, "number_count2", self.callback_sensor, 10)
        
        # 1. Setup do FMPy
        self.model_description = fmpy.read_model_description(fmu_path)
        self.unzipdir = fmpy.extract(fmu_path)
        
        # Mapeamento de referências (v_refs) - as variáveis que você listou
        self.v_refs = {v.name: v.valueReference for v in self.model_description.modelVariables}
        
        # 2. Instanciar (SEM 'kind' ou 'fmu_type' para evitar conflito de versão)
        # O FMPy vai ler do model_description se é CoSimulation
        self.fmu_instance = instantiate_fmu(
            unzipdir=self.unzipdir,
            model_description=self.model_description
        )
        
        # 3. Inicialização
        self.fmu_instance.setupExperiment(startTime=0.0)
        self.fmu_instance.enterInitializationMode()
        self.fmu_instance.exitInitializationMode()
        
        self.current_time = 0.0
        self.dt = 0.01
        

    def callback_sensor(self, msg):
        try:
            # Seta a entrada 'u'
            self.fmu_instance.setReal([self.v_refs['u']], [float(msg.data)])
            self.get_logger().info(f"Received {msg.data}")
            # Passo de simulação
            self.fmu_instance.doStep(currentCommunicationPoint=self.current_time, communicationStepSize=self.dt)
            self.current_time += self.dt
            
            # Pega a saída 'y'
            y_val = self.fmu_instance.getReal([self.v_refs['y']])[0]
            
            out_msg = Int64()
            out_msg.data = int(y_val)
            self.get_logger().info(f" output= {self.current_time:.2f} s, y={y_val:.2f}")
            self.pub_out.publish(out_msg)
        except Exception as e:
            self.get_logger().error(f"Erro no passo do FMU: {e}")

    def destroy_node(self):
        self.fmu_instance.terminate()
        self.fmu_instance.freeInstance()
        fmpy.util.clean_temporary_dir(self.unzipdir)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = FMUControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()