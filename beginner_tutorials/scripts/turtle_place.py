#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

from turtlesim.msg import Pose

def callback(msg):
    if msg.x <= 1.0 or msg.x >= 10.0 or msg.y <= 1.0 or msg.y >= 10.0:
        rospy.logwarn("경고 (x: %.2f, y: %.2f)", msg.x, msg.y)
 
 
def monitor_turtle():
   
    rospy.init_node('turtle_position_monitor', anonymous=True)

    
    rospy.Subscriber('/turtle1/pose', Pose, callback)

    
    rospy.spin()

if __name__ == '__main__':
    try:
        monitor_turtle()
    except rospy.ROSInterruptException:
        pass