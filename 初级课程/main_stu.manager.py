'''
这是一个主程序文件，用来实现程序的入口
'''
#因为主程序就是用来进行学生信息管理的，必然需要导入学生管理模块
from p_12学生管理模块 import *

#设置入口
if __name__ == '__main__':
    sms=Studentmanagersystem()
    sms.start()