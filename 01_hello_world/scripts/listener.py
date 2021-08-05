#!/usr/bin/env python
#coding=utf8

import rospy
from std_msgs.msg import String


class listner():
    def __init__(self):
        rospy.init_node("listener", anonymous=False)
        rospy.on_shutdown(self.shutdown)
        rospy.Subscriber("/hello_msg", String, callback=self.hello_cb)

    def hello_cb(self, data):
        rospy.loginfo('listenning: %s' % data.data)
        rospy.logwarn('listenning: %s ' % data.data)


    def shutdown(self):
        rospy.loginfo('bye')
        pass


if __name__ == "__main__":
    obj = listner()
    rospy.spin()
