#!/usr/bin/env python

import time
import rospy
from pymavlink import mavutil
from std_msgs.msg import Float32, Int32

def get_depth():
	master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
	master.wait_heartbeat()
	depth = master.messages['LOCAL_POSITION_NED'].z
	depth = round(depth, 4)
	return depth

def get_battery_status():
	master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
	master.wait_heartbeat()
	battery = master.messages['BATTERY_STATUS'].battery_remaining
	return battery

def publish_data():
	rospy.init_node('ardusub_publisher_node', anonymous=True)
	depth_pub = rospy.Publisher('rov_depth', Float32, queue_size=10)
	battery_pub = rospy.Publisher('rem_battery', Int32, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		try:
			depth = get_depth()
			rem_battery = get_battery_status()
			battery_pub.publish(rem_battery)
			depth_pub.publish(depth)
		except:
			pass
		rate.sleep()

if __name__ == '__main__':
	try:
		publish_data()
	except rospy.ROSInterruptException:
		pass
