'''
多态性，python天生多态
同一个方法名，传入不同的参数（传入不同的对象），得到了不同的结果，就叫多态
'''
class Father(object):
    def cure(self):
        print('老中医使用中医治病')

class Son(Father):
    def cure(self):
        print('儿子采用西医治病')

class Dog(object):
    def bark(self):
        print('wolf,wolf,wolf')

class Patient(object):
    def need_doctor(self,doctor):
        doctor.cure()

a=Patient()
a.need_doctor(Father())
a.need_doctor(Son())



'''
实例属性和实例方法
'''

class Cat(object):
    #定义一个属性
    def __init__(self,name):
        self.name=name
    #定义一个方法
    def info(self):
        print(self.name)
    #定义一个方法
    def show(self):
        print('SHOW run')
        #在实例方法中调用其他的实例方法，需要用到self
        self.info()

# mimi=Cat('Mimi')
# print(mimi.name)
# print('*'*10)
# mimi.info()
# print('*'*10)
# mimi.show()

tom=Cat('Tom')
print(tom.name)
tom.show()
# print(Cat.name)
# 类名不能调用实例属性和实例方法，原因是有类对象存在时，但不一定有实例对象
#只有实例对象才能调用实例属性和实例方法

'''
类属性和类方法
'''

class Classroom(object):
    #定义一个类属性
    center_kong_tiao='格力空调'#这个类属性相当于类中的全局变量，该类的所有对象都可以使用该属性,以此在所有对
                             #象之间进行数据共享

cr901=Classroom()
print(cr901.center_kong_tiao)

cr902=Classroom()
print(cr902.center_kong_tiao)

#修改数据，进行对象间数据共享
Classroom.center_kong_tiao='BAIXUE'  #类对象.类属性 来更改
print(cr901.center_kong_tiao)
print(cr902.center_kong_tiao)

#类属性可以使用实例对象来引用，但不能更改
#一般情况下，类属性都只使用类对象来调用

