#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np
import matplotlib.pyplot as plt
import math

#Publisher
def talker():

    print 'pub node : talker'
    rospy.init_node('pub', anonymous=True)
    pub = rospy.Publisher('hello1_msg', String, queue_size=10)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():

        message = "hello world"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


#executable
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


