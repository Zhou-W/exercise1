#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32

def callback(msg):
    exercise1_pub2 = rospy.Publisher('kthfs/reslut',Float32,queue_size=10)
    k=msg.data
    rospy.loginfo("nodeB = %s",k/0.15)
    exercise1_pub2.publish(k/0.15)

def listener():
    rospy.init_node('listener',anonymous=True)
    exercise1_sub = rospy.Subscriber('Zhou',Int32,callback)
    rospy.spin()
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
