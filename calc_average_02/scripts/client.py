#!/usr/bin/env python
#coding=utf8

import rospy
from calc_average_02.srv import calcAvg, calcAvgRequest, calcAvgResponse


class client():
    def __init__(self):
        rospy.init_node("avg_client", anonymous=False)
        rospy.on_shutdown(self.shutdown)
        rospy.loginfo('waiting server')
        rospy.wait_for_service("/calcAvg")
        rospy.loginfo('sever is ok')
        self.client = rospy.ServiceProxy("/calcAvg", calcAvg)

    def calc(self, x, y, z):
        res = self.client.call(x, y, z)
        return res

    def shutdown(self):
        rospy.loginfo('bye')
        pass


if __name__ == "__main__":
    obj = client()

    num1 = 1.0
    num2 = 1.0
    num3 = 1.0

    avg1 = obj.calc(num1, num2, num3)
    rospy.loginfo('result: [(%s + %s + %s) / 3.0 = %s]' %
                  (num1, num2, num3, avg1))

    num1 = 19
    avg2 = obj.calc(num1, num2, num3)
    rospy.loginfo('result: [(%s + %s + %s) / 3.0 = %s]' %
                  (num1, num2, num3, avg2))

    num2 = -17
    avg3 = obj.calc(num1, num2, num3)
    rospy.loginfo('result: [(%s + %s + %s) / 3.0 = %s]' %
                  (num1, num2, num3, avg3))
