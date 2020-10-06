#!/usr/bin/env python

import rospy
from hector_uav_msgs.msg import PoseActionGoal

rospy.init_node('move_up')
pub = rospy.Publisher('action/pose/goal', PoseActionGoal, queue_size=10)
move = PoseActionGoal()
move.goal.target_pose.header.frame_id = 'world'
move.goal.target_pose.pose.position.z = 2.0
pub.publish(move)
