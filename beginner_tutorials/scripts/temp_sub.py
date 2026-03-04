#!/usr/bin/env python3

import rospy

from std_msgs.msg import Float64

def callback(msg):

    if msg.data <35:
        rospy.loginfo("수신: %f", msg.data)
    else:
        rospy.loginfo("35.0도 경고")
    

def listener():

    rospy.init_node('counter_sub')

    rospy.Subscriber('counter', Float64, callback)

    rospy.spin()

if __name__ == '__main__':

    listener()
