import VL53L0X
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
#from rcl_interfaces.msg import SetParametersResult

class TOFRosPublisher(Node) :

    def __init__(self):
        super().__init__('tof_ros_publisher_node')

        self.declare_parameter("epuck-name","epuck")

        self.tof = VL53L0X.VL53L0X(i2c_bus=4,i2c_address=0x29)
        self.tof.open()
        self.accuracy_mode = VL53L0X.Vl53l0xAccuracyMode.BETTER # change mode here if you want to use different accuracy modes
        self.tof.start_ranging(self.accuracy_mode)
        self.pub = self.create_publisher(Int16,self.get_parameter("epuck-name").get_parameter_value().string_value + '/tof',1)
        self.timer = self.create_timer(0.1,self.cb)

    def cb(self):
        distance = self.tof.get_distance()
        msg = Int16()
        msg._data = distance
        self.pub.publish(msg)
    
    def clean(self):
        self.tof.stop_ranging()
        self.tof.close()
    
    # def parameter_callback(self, params) -> None:
    #     for param in params:
    #         if(param.name == "run"):
    #             if(not param.value and self.run): self.stop()
    #             elif(param.value and not self.run): self.tof.start_ranging(self.accuracy_mode)

    #     return SetParametersResult(successful=True)
    
def main(args=None):
    rclpy.init(args=args)
    node = TOFRosPublisher()
    rclpy.spin(node)
    node.clean()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


    
    