#定义一个父类
class Phone(object):
    #定义一个属性name
    def __init__(self):
        self.name='电话'
    #定义一个打电话的方法
    def call(self,number):
        print(f'正在给{number}打电话')

#继承出一个子类
class Iphone(Phone):
    # pass #此时与父类完全相同
    #在子类中定义一个拍照方法
    def camera(self):
        print(f'正在拍照')


#当发生继承时，子类会继承父类的属性和方法，可以直接使用
iphonex=Iphone()
iphonex.call('13564895652')
iphonex.camera()
print(iphonex.name)