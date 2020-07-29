#!/usr/bin/env python

import rospy
import random
from my_package.msg import my_float32

def talker():
	rospy.init_node('publisher', anonymous=True)
	pub = rospy.Publisher('my_random_float', my_float32, queue_size=10)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		num = my_float32()
		num.data = random.random()
		pub.publish(num)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
