#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class talker():
    def __init__(self):
        rospy.init_node("talker", anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.pub = rospy.Publisher("/hello_msg", String, queue_size=5)
        self.r = rospy.Rate(1)

        hello = String()
        start = rospy.get_time()
        while not rospy.is_shutdown():
            now = rospy.get_time()
            hello.data = 'hello world %.2f s' % (now - start)
            self.pub.publish(hello)
            self.r.sleep()

    def shutdown(self):
        rospy.loginfo('bye talker')
        rospy.sleep(1.0)


if __name__ == "__main__":
    obj = talker()
    rospy.spin()
