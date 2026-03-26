#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String  

class WallFollowerPID:
    def __init__(self):
        rospy.init_node('wall_follower_pid')
        
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.led_pub = rospy.Publisher('/led_color', String, queue_size=1)
        self.cmd_sub = rospy.Subscriber('/cmd_vel', Twist, self.cmd_callback)
        
        self.is_backing_up = False

    def get_range(self, scan, angle):
        index = int((angle - scan.angle_min) / scan.angle_increment)
        index = max(0, min(index, len(scan.ranges) - 1))
        distance = scan.ranges[index]
        if math.isnan(distance) or math.isinf(distance):
            distance = 10.0
        return distance

   
    def cmd_callback(self, twist):
        
        if twist.linear.x < 0.0:
            self.is_backing_up = True
        else:
            self.is_backing_up = False

    def scan_callback(self, scan):
        front = self.get_range(scan, 0.0)
        
    
        if self.is_backing_up:
            color = "RED"

        elif front < 0.5:
            color = "BLUE"

        else:
            color = "GREEN"
            
        
        self.led_pub.publish(color)
            
if __name__ == '__main__':
    try:
        wf = WallFollowerPID()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass