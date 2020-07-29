#!/usr/bin/env python

import rospy

def main_node():
	rospy.init_node('chatter', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		print("Hello Samarth")
		rate.sleep()

if __name__ == '__main__':
	try:
		main_node()
	except rospy.ROSInterruptException:
		pass
