#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np
import matplotlib.pyplot as plt
import math
import time



#data = hello world (from sub.py)
def callback(data):
    time.sleep(1)
    rospy.loginfo("Finally i got the %s", data.data) 

#subscriber 
def listener():

    rospy.init_node('mainsub')
    rospy.Subscriber('hello2_msg', String, callback)

#executable
if __name__ == '__main__':
    try:
        listener()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

