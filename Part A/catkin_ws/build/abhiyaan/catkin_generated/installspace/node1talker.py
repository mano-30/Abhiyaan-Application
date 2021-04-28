#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
 
def talker():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10)
    rospy.init_node('node1talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_str = "Team Abhiyaan: %s" % rospy.get_time()
        rospy.loginfo(pub_str)
        pub.publish(pub_str)
        rate.sleep()
  
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
