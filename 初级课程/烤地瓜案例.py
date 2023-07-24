#定义一个地瓜类
class Sweetpotato(object):
    #用__init__方法进行初始化，初始化地瓜的状态，烧烤总时间，以及调料
    def __init__(self):
        self.status='生地瓜'
        self.cook_totaltime=0
        self.tiaoliao=[]
    #定义一个烧烤方法,给参数cook_time
    def cook(self,cook_time):
        self.cook_totaltime=self.cook_totaltime + cook_time
        if self.cook_totaltime<3:
            self.status='生地瓜'
        elif self.cook_totaltime<6:
            self.status='半生不熟'
        elif self.cook_totaltime<9:
            self.status='熟地瓜'
        else:
            self.status='烤成炭'
    #定义一个加调料方法
    def addcondiment(self,tl):
        self.tiaoliao.append(tl)

    #定义__str__()方法，方便print()输出
    def __str__(self):

        s=self.status+('考了%dmin\n' %self.cook_totaltime)+'加了以下调料：\n'
        for i in self.tiaoliao:
            s+=i+'\n'
        return s
#全部定义好之后，开始实例对象
sp1=Sweetpotato()
sp2=Sweetpotato()
#实例对象之后开始调用类中的方法
sp1.cook(2)
sp1.addcondiment('蜂蜜')
sp1.cook(4)
sp1.addcondiment('酱油')
print(sp1)

sp2.cook(4)
sp2.addcondiment('老干妈')
sp2.cook(5)
sp2.addcondiment('芥末油')
print(sp2)