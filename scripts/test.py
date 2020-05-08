#! /usr/bin/env python
#coding=utf-8

import rospy
from rubik_cube_solve.srv import rubik_cube_solve_cmd
import random

rospy.init_node("rubik_cube_slove_test")
client = rospy.ServiceProxy("/analyse_rubik_cube_cmd", rubik_cube_solve_cmd)
rospy.wait_for_service("analyse_rubik_cube_cmd")
rospy.Duration(5)
rate = rospy.Rate(1);
random.seed()
cnt = 0
while not rospy.is_shutdown():
    i = random.randint(1, 6)
    rospy.loginfo("face: %d", i)
    client.call(i, 180)
    cnt += 1
    rospy.loginfo("cnt: %d", cnt)
    rate.sleep()