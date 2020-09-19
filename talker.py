#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def talker():
    rospy.init_node('talker',anonymous=True)
    exercise1_pub = rospy.Publisher('Zhou',Int32,queue_size=10)
    rate = rospy.Rate(20)

    k = 1
    while not rospy.is_shutdown():
        exercise1_pub.publish(k)
        rospy.loginfo("NodeA = %s",k)
        rate.sleep()
        k = k + 4

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass