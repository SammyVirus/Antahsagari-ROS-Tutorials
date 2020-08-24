#!/usr/bin/env python

import rospy
from pymavlink import mavutil
from sensor_msgs.msg import BatteryState

present_battery_status = BatteryState()

def get_battery_status():
	master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
	master.wait_heartbeat()
	battery_status = master.messages['SYS_STATUS']
	cell_voltage = master.messages['BATTERY_STATUS'].voltages
	return cell_voltage, battery_status

def publish_battery_status():
	rospy.init_node('battery_status_node', anonymous=True)
	pub = rospy.Publisher('battery_status', BatteryState, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		try:
			cell_voltage, battery_status = get_battery_status()
			present_battery_status.percentage = battery_status.battery_remaining
			present_battery_status.current = battery_status.current_battery
			present_battery_status.voltage = battery_status.voltage_battery
			present_battery_status.cell_voltage = cell_voltage
			pub.publish(present_battery_status)
		except:
			pass
		rate.sleep()

if __name__ == '__main__':
	try:
		publish_battery_status()
	except rospy.ROSInterruptException:
		pass





