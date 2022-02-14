import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SettingsPublisher(Node):

    def __init__(self) -> None:
        super().__init__('SettingsPublisher')
        self.publisher_ = self.create_publisher(String, 'RBW_settings', 10)

    def publishSettings(self, settings):
        msg = String()
        msg.data = settings
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    print("////// Settings change //////" )
    RBW = str(input("Input RBW value (in KHz): "))
    SettingsPub = SettingsPublisher()

    SettingsPub.publishSettings(RBW)

    SettingsPub.destroy_node()
    rclpy.shutdown()
    return 0   

if __name__ == '__main__':
    main()