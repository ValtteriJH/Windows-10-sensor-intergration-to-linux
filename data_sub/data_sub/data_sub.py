from ctypes.wintypes import MSG
import imp
from socket import MsgFlag
from time import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from data_msg.msg import Msg

class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Msg,
            'data',
            self.listener_callback,
            10)
        self.subscription 

    def listener_callback(self, msg):
        time = self.get_clock().now().to_msg()
        #print(time)
        sec = time.sec - msg.stamp.sec
        nsec =  time.nanosec - msg.stamp.nanosec 
        # seconds and nanoseconds are calculated as epoch time 
        # it must divided with 60 to get current seconds 
        self.get_logger().info(str((sec + (nsec * 10**(-9))) % 60)) 



def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)    
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
