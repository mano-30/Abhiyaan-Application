#!/usr/bin/env python
import rospy
from std_msgs.msg import String

msgs = list()

def callback1(data):
   
    msgs[0] = data

def callback2(data):
   
    msgs[1] = data

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("team_abhiyaan", String,callback1)
    rospy.Subscriber("autonomy",String,callback2)
    
    rospy.loginfo(rospy.get_caller_id() + "I heard %s %s",msgs[0].data,msgs[1].data)
    msgs.clear()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
