#!/usr/bin/env python

import rospy
from hector_uav_msgs.msg import PoseActionGoal

rospy.init_node('move_up')
pub = rospy.Publisher('action/pose/goal', PoseActionGoal, queue_size=10)
rate = rospy.Rate(2)
move = PoseActionGoal()
move.goal.target_pose.header.frame_id = 'world'
move.goal.target_pose.pose.position.z = 1.0

success=1
while not rospy.is_shutdown():
  if success<=2:
    pub.publish(move)
    rate.sleep()
    success+=1
