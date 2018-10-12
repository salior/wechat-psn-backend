# -*- coding:utf-8 -*-
import werobot
robot = werobot.WeRoBot(token='testrobot')  #token="testrobot"
@robot.text
def echo(message):
    return message.content
robot.config['HOST'] = '0.0.0.0' #默认允许所有IP访问
robot.config['PORT'] = 80  #指定80端口
robot.run()
