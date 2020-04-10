#!/usr/bin/env python  

import rospy
### Import correct framework here ###
from std_msgs.msg import Int16
from lab_1.msg import TwoInts
### End import framework here ###



def callback(data):
	### Add your code here ###
	msg = data.a + data.b
	rospy.loginfo(str(data.a) + " + " + str(data.b) + " = " + str(msg))
	pub.publish(msg)
	### End your code here ###

def talker_listener():
	
	rospy.init_node('two_ints_listener_node', anonymous=True)
	
	global pub
	### Add your code here ###
	pub = rospy.Publisher('/sum', Int16,queue_size=1)
	rospy.Subscriber('/two_ints', TwoInts, callback) 
	### End your code here ###

	rospy.spin()

if __name__ == '__main__':
	try:
		talker_listener()
	except rospy.ROSInterruptException:
		raise e
