
import rclpy
from rclpy.node import Node


class position_node(Node):
    def __init__(self): 
        super().__init__("second_node")
        self.get_logger().info("start!")
def main(args=None):
    rclpy.init(args=args)
    node=position_node()
    rclpy.spin(node)
    rclpy.shutdown()
    
    if __name__=="__main__":
        main()