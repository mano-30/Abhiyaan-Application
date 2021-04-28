#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
PI = 3.1415926535897
choice = 1

global x = 0
global y = 5.4

def move(x,y,speed):
    # Starts a new node
    rospy.init_node('turtleovertake', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()


    vel_msg.linear.x = abs(speed)

    #Since we are moving just in x-axis
    vel_msg.linear.y = 0 
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance<3.44445):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        x = current_distance
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

def rotate(speed,angle):
    #Starts a new node
    rospy.init_node('turtleovertake', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    
    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    
    vel_msg.linear.x= speed*math.cos(current_angle)
    vel_msg.linear.y= speed*math.cos(current_angle)
    t0 = rospy.Time.now().to_sec()
    current_dist = 0
    
    while(current.distance!=2):
        
       #Publish the velocity
       velocity_publisher.publish(vel_msg)
       #Takes actual time to velocity calculus
       t1=rospy.Time.now().to_sec()
       #Calculates distancePoseStamped
       current_distance= math.sqrt(math.pow(vel_msg.linear.x*(t1-t0),2)+math.pow(vel_msg.linear.y*(t1-t0),2))
   
    x = current_distance*math.cos(angle)
    y = current_distance*math.sin(angle)
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    velocity_publisher.publish(vel_msg)
    vel_msg.angular.z = abs(angular_speed)

    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
  
  
    while(current_angle > 0):
       
       velocity_publisher.publish(vel_msg)
       t1 = rospy.Time.now().to_sec()
       current_angle = current_angle-angular_speed*(t1-t0)

    rospy.spin()

if __name__ == '__main__':
    
    print("Let's move your robot")
    speed = float(input("Input your speed to move forward:"))
    ang_speed = float(input("Input your speed to rotate in deg/sec")
    angle = float(input("Input angle to rotate in degrees:"))
    try:
        #Testing our function
        move(speed)
        rotate(ang_speed,angle)
        move(speed)
    except rospy.ROSInterruptException: pass
