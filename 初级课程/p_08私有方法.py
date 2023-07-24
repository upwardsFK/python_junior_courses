'''
私有方法
'''
class Thunderbird(object):
    #初始化下载列表
    def __init__(self):
        self.list=[]
    #核心代码，下载，需隐藏，不可见
    def __download(self,wz):
        print(f'通过{wz}网址正在下载中')

    #通过添加工作进入列表中，间接开始下载
    def add_work(self,wz):
        self.list.append(wz)
        self.__download(wz)#__download(tb,wz)

tb=Thunderbird()
tb.add_work('http://hebuster/‘校园美景.mp4')

