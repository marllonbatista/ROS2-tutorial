import rclpy
from rclpy.node import Node
from geometry_msgs.msg import  Twist

class controller_vel(Node):
    pass
def main (args=None):
    rclpy.init(args=args)#inicia a comunicação
    node=controller_vel()
    rclpy.spin(node)#deixa o node ativo 
    rclpy.shutdown()#fecha a comunicação
    
    if __name__== '__main__':
        main()