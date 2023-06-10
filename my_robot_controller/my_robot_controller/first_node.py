
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import  Twist

class controller_vel(Node):
    def __init__(self):
        super().__init__("first_node")
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1.0,self.callback_vel)
        self.counter=0
    def callback_vel(self):
        msg=Twist()
        self.counter+=1
        if self.counter == 1:
            msg.linear.x=2.0
            msg.linear.y=0.0
        elif self.counter == 2:
            msg.linear.x=0.0
            msg.linear.y=3.0
        elif self.counter == 3:
            msg.linear.x=-2.0
            msg.linear.y=0.0
        elif self.counter == 4:
            msg.linear.x=0.0
            msg.linear.y=-3.0
            self.counter=0
        self.cmd_vel_pub.publish(msg)
        
def main (args=None):
    rclpy.init(args=args)#inicia a comunicação
    node=controller_vel()
    rclpy.spin(node)#deixa o node ativo 
    rclpy.shutdown()#fecha a comunicação
    
    if __name__== '__main__':
        main()
