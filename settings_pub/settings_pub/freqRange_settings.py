import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SettingsPublisher(Node):

    def __init__(self) -> None:
        super().__init__('SettingsPublisher')
        self.publisher_ = self.create_publisher(String, 'freqRange_settings', 10)

    def publishSettings(self, settings):
        msg = String()
        msg.data = settings
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    right = False
    while right:
        rclpy.init(args=args)
        print("////// Settings change //////" )
        start = str(input("Input starting frequancy (min freq 62) (in GHz): "))
        stop = str(input("Input stopping frequancy (min freq 69) (in GHz): "))
        if (start >= 62 and stop <= 69 and start < stop):
            right = True
            
    start_stop = "[" + start + "," + stop + "]"
    SettingsPub = SettingsPublisher()
    SettingsPub.publishSettings(start_stop)

    SettingsPub.destroy_node()
    rclpy.shutdown()
    return 0  

if __name__ == '__main__':
    main()