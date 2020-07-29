#!/usr/bin/env python

import rospy
import numpy as np
from my_package.msg import my_float32

log_value = my_float32()
def calculate_log(msg):
	log_value.data = np.log(msg.data)

def listener():
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber('my_random_float', my_float32, calculate_log)
	pub = rospy.Publisher('random_float_log', my_float32, queue_size=10)
	rate = rospy.Rate(10)	

	while not rospy.is_shutdown():
		pub.publish(log_value)
		rate.sleep()


if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

