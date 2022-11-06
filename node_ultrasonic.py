#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Float32
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard {}".format(data.data))

def ultrasonicListener():
    rospy.init_node('ultrasonic_listener')

    listener = rospy.Subscriber('sonar',Float32,callback)
    
    rospy.spin()

if __name__ == '__main__':
    ultrasonicListener()
    
    
