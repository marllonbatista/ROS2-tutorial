import rclpy
from rclpy.node import Node
from geometry_msgs.msg import  Twist
from turtlesim.msg import Pose

class turtlecontroller (Node):
    def __init__(self) :
        super().__init__("third_node")
        self.publi=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.subscript=self.create_subscription(Pose,"/turtle1/pose",self.controller_callback,10)
    def controller_callback(self,pose:Pose):
        
        msg_vel=Twist()
        if pose.x < 10.0 and pose.y<5.55:
            msg_vel.linear.x=2.0
            msg_vel.linear.y=0.0
        elif pose.x>10.0 and pose.y<10.0:
            msg_vel.linear.x=0.0
            msg_vel.linear.y=2.0
        elif pose.y >10.0 and pose.x > 5.5:
            msg_vel.linear.x=-2.0
            msg_vel.linear.y=0.0
        elif pose.x<5.5 and pose.y > 5.6:
            msg_vel.linear.x=0.0
            msg_vel.linear.y=-2.0
        self.publi.publish(msg_vel)
        
def main(args=None):
    rclpy.init(args=args)
    node=turtlecontroller()
    rclpy.spin(node)
    rclpy.shutdown()

    if __name__=="__main__":
        main()