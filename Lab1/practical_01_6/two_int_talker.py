#!/usr/bin/env python  
import random
import rospy

### Import correct framework here ###
from std_msgs.msg import Int16
from lab_1.msg import TwoInts
### End import framework here ###

def talker():
    pub = rospy.Publisher('/two_ints', TwoInts, queue_size=10)
    rospy.init_node('two_int_talker_node', anonymous=True)

    ### Add your code here ###
    rate = rospy.Rate(0.5)
    ### End your code here ###    

    random.seed()

    while not rospy.is_shutdown():
	
	### Add your code here ###
	msg = TwoInts()
        msg.a = random.randint(1,20)
        msg.b = random.randint(1,20)
	rospy.loginfo(msg.a)
	### End your code here ###

	pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



        
