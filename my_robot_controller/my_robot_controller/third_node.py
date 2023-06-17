import rclpy
from rclpy.node import Node
from geometry_msgs.msg import  Twist
from turtlesim.msg import Pose

class turtlecontroller (Node):
    def __init__(self) :
        super().__init__("third_node")
        self.get_logger().info("start")
def main(args=None):
    rclpy.init(args=args)
    node=turtlecontroller()
    rclpy.spin(node)
    rclpy.shutdown()

    if __name__=="__main__":
        main()