#!/usr/bin/env python
#coding=utf8

import rospy
from calc_average_02.srv import calcAvg, calcAvgRequest, calcAvgResponse


class server():
    def __init__(self):
        rospy.init_node("avg_server", anonymous=False)
        rospy.on_shutdown(self.shutdown)
        rospy.Service("calcAvg", calcAvg, handler=self.handle_calcAvg)

    def handle_calcAvg(self, req):
        # type:(calcAvgRequest)
        rospy.loginfo('calculating: [(%s + %s + %s) / 3.0 = ]' %
                      (req.num1, req.num2, req.num3))
        res = (req.num1 + req.num2 + req.num3) / 3.0
        rospy.loginfo('result is %s' % res)
        return calcAvgResponse(res)

    def shutdown(self):
        rospy.loginfo('bye')
        pass


if __name__ == "__main__":
    obj = server()
    rospy.spin()