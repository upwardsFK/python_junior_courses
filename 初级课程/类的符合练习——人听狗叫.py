'''
类的符合练习
人想听狗叫
'''
#创建狗类，方法为叫
class Dog(object):
    #采用init方法为狗类绑定属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #添加另一个方法，叫,并给定叫的次数n
    def bark(self,n):
        for i in range(n):
            print('wolf')

#创建人类
class Person(object):
    #采用init方法为人类绑定属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #为人类添加狗
    def add_dog(self,pet):
        self.dog=pet  #Tom.dog=Dog('yoyo',2)
    #人听狗叫,并规定次数
    def listen_bark(self,n):
        self.dog.bark(n)   #yoyo.bark(n)

#实例对象
Tom=Person('Tom',11)
Tom.add_dog(Dog('yoyo',2))
Tom.listen_bark(5)

