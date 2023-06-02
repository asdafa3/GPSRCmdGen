#!/usr/bin/env python
import rospy
import argparse
import os
from std_msgs.msg import String
import time


parser = argparse.ArgumentParser(
				prog='check_grammer',
				description='Send each line of a file to psa')
parser.add_argument('filename')  
args = parser.parse_args()

if hasattr(args,'help') and args.help:
	parser.print_help()
	parser.exit(1)

rospy.init_node('node_name')

pub = rospy.Publisher('/ps_adapter/custom_rec', String, queue_size=10)
r = rospy.Rate(10)

time.sleep( 2 )

file1 = open(args.filename, 'r')
Lines = file1.readlines()
for line in Lines:
	line = line.replace(",", "")
	line = line.replace("'s", "s")
	pub.publish(line.lower().strip())
	r.sleep()

