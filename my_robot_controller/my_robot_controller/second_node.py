
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class position_node(Node):
    def __init__(self): 
        super().__init__("second_node")
        self.pose_subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.pose_subscriber
        
    def pose_callback(self,msg:Pose):
        self.get_logger().info(str(msg.x))
def main(args=None):
    rclpy.init(args=args)
    node=position_node()
    rclpy.spin(node)
    rclpy.shutdown()
    
    if __name__=="__main__":
        main()