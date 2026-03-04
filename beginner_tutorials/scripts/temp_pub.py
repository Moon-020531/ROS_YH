#!/usr/bin/env python3

import rospy

from std_msgs.msg import Float64

import random

def counter():

    pub = rospy.Publisher('counter', Float64, queue_size=10)

    rospy.init_node('counter_pub')

    rate = rospy.Rate(1)  # 1Hz = 1초에 1번


    while not rospy.is_shutdown():

        count = random.uniform(20.0, 40.0)

        rospy.loginfo("발행: %f", count)

        pub.publish(count)

        

        rate.sleep()

if __name__ == '__main__':

    try:

        counter()

    except rospy.ROSInterruptException:

        pass
