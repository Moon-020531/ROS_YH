#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def counter():
    
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_move_node') 
    rate = rospy.Rate(1)  # 1초에 1번 실행

  
    vel_msg = Twist()

    vel_msg.linear.x = 2.0  
    vel_msg.angular.z = 2.0 

   
    while not rospy.is_shutdown():
        pub.publish(vel_msg) 
        rate.sleep()         

if __name__ == '__main__':
    try:
        counter()
    except rospy.ROSInterruptException:
        pass