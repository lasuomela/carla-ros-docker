from copy import deepcopy
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor 

import random
import math
import transforms3d as t3d

#from std_msgs.msg import String
from nav_msgs.msg import Odometry as msg_type
from geometry_msgs.msg import Quaternion


def add_noise_to_pose(odometry_msg, pos_noise_magnitude, ang_noise_magnitude):

    position = odometry_msg.pose.pose.position
    position.x = position.x +random.uniform(-pos_noise_magnitude, pos_noise_magnitude)
    position.y = position.y +random.uniform(-pos_noise_magnitude, pos_noise_magnitude)

    orientation = odometry_msg.pose.pose.orientation

    orientation_t3d = [orientation.w, orientation.x, orientation.y, orientation.z]

    angle_offset_rad = random.uniform(-ang_noise_magnitude,ang_noise_magnitude)*(2*math.pi/360)
    angle_offset_quat = t3d.euler.euler2quat(0, 0, angle_offset_rad)

    new_quat = t3d.quaternions.qmult(angle_offset_quat, orientation_t3d)
    new_quat = new_quat/t3d.quaternions.qnorm(new_quat)

    new_orientation = Quaternion()
    new_orientation.w = new_quat[0]
    new_orientation.x = new_quat[1]
    new_orientation.y = new_quat[2]
    new_orientation.z = new_quat[3]

    odometry_msg.pose.pose.orientation = new_orientation



class MinimalPublisher(Node):

    def __init__(self, topic_name):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(msg_type, topic_name, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0
        self.msg = None

    def timer_callback(self):
        #msg = String()
        #msg.data = 'Hello World: %d' % self.i 
        if self.msg is not None:
            self.get_logger().info('Publishing: "%s"' % self.msg.child_frame_id)
            self.publisher_.publish(self.msg)
        else:
            self.get_logger().info('Msg is None')
        #self.i += 1

    def set_data(self, msg):
        self.get_logger().info('Pub: got "%s"' % msg.child_frame_id)

        add_noise_to_pose(msg, 0.5, 15)
        self.msg = msg

class MinimalSubscriber(Node):

    def __init__(self, pub, topic_name):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            msg_type,
            topic_name,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pub = pub
        

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.child_frame_id)
        self.pub.set_data(deepcopy(msg))


def main(args=None):
    rclpy.init(args=args)
    pub_name = '/carla/ego_vehicle/odometry_mod'
    sub_name = '/carla/ego_vehicle/odometry'
    minimal_publisher = MinimalPublisher(pub_name)
    minimal_subscriber = MinimalSubscriber(minimal_publisher, sub_name)

    executor = SingleThreadedExecutor()
    executor.add_node(minimal_publisher)
    executor.add_node(minimal_subscriber)

    executor.spin()
    #rclpy.spin(minimal_publisher)
    #rclpy.spin(minimal_subscriber)
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()