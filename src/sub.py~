#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np
import matplotlib.pyplot as plt
import math
import time



#data = hello world (from pub.py)
def callback(data):
    time.sleep(1)
    rospy.loginfo("i got the %s", data.data) #receive pub

#subscriber 
def listener():

    print 'sub node : listener'
    rospy.init_node('sub')
    rospy.Subscriber('hello1_msg', String, callback)

#Publisher
def talker():

    print 'sub node : talker'
    rospy.init_node('sub')
    pub = rospy.Publisher('hello2_msg', String, queue_size=10)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():

        message = "hello world"
        #rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


#executable
if __name__ == '__main__':
    try:
        listener()
        talker()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

