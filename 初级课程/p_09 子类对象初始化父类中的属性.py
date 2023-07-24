'''
子类对象初始化父类中的属性
'''
#创建一个父类
class Father(object):
    def __init__(self,name):
        self.name=name

#创建一个子类
class Son(Father):
    #因为子类提供了init方法，那么在使用子类实例对象时，就会调用自己的init方法，
    #那么就不会调用父类中的init方法，父类中的属性name就无法绑定
    #如果想要绑定，就需要手动调用父类中的init方法

    def __init__(self,age,name):
        self.age=age
        Father.__init__(self,name)#手动输入self

#实例对象
#子类中有init方法，就使用子类中的，且父类的init不可用；子类中没有init方法，就使用父类的
Tom=Son(19,'Tom')
print(Tom.age)
print(Tom.name)
# print(Tom.name)  #AttributeError: 'Son' object has no attribute 'name'

print('*'*10)

'''
子类当中重写和调用父类的方法
'''
#重写是指子类继承父类中的公有属性和公有方法之后，在子类中写一个和父类中名称完全一样，但内容不同的属性或方法，就叫做重写
#定义一个父类
class Father(object):
    #定义一个治疗方法
    def cure(self):
        print('父类采用中医治疗')

#定义一个子类
class Son(Father):
    #定义一个治疗方法
    def cure(self):#继承了父类的治疗方法，子类又自己写了一个同名的方法，并对其中内容进行修改————重写
        Father.cure(self)  #先让父类进行cure，之后再子类进行，直接调用父类中的cure方法，手动传参self
        print('子类采用西药治病')

#实例一个子类对象
s=Son()
s.cure()


'''
多继承
多层继承为纵向关系，多继承为横向关系
'''
# #定义一个父亲类
# class Father(object):
#     def show_fa(self):
#         print('fa.fun run...')
#
# #定义一个母亲类
# class Mother(object):
#     def show_mo(self):
#         print('mo.fun run...')
#
# #定义一个以上两者的子类
# class Son(Father,Mother):
#     def play(self):
#         print('so.fun run...')
#
# #实例一个子类对象
# s=Son()
#

'''
多继承的初始化问题
'''

#下面这种继承方式称为钻石继承（又称为菱形继承）
#这种继承关系上，共同的父类Person()会被初始化多次，这是继承中的问题
#原因是父类名调用初始化方法的时候引起的
# class Person(object):
#     def __init__(self,aaa):
#         self.aaa=aaa  #s.aaa=1
#
#
# class Father(Person):
#     def __init__(self,aaa,name):
#         Person.__init__(self,aaa)
#         self.name=name
#
# class Mother(Person):
#     def __init__(self,aaa,age):
#         Person.__init__(self, aaa)
#         self.age=age
#
# class Son(Father,Mother):
#     def __init__(self,aaa,name,gender,age):
#         Father.__init__(self,aaa,name)
#         Mother.__init__(self,aaa,age)
#         self.gender=gender
#
# #实例一个子类对象
# s=Son(1,'Tom','男',17)
#

'''
钻石继承问题的解决
'''
class Person(object):
    def __init__(self,aaa):#aaa : age=11,aaa=2; name='Tom',aaa=2
        self.aaa=aaa #self.aaa= *args


class Father(Person):
    def __init__(self,name,*args):
        super().__init__(*args)  #*args 手动解包
        self.name=name

class Mother(Person):
    def __init__(self,age,*args):
        super().__init__(*args)
        self.age=age

class Son(Father,Mother):
    def __init__(self,gender,name,age,aaa):  #按mro顺序
        super().__init__(name,age,aaa)
        self.gender=gender

#实例一个子类对象
s=Son('男','Tom',11,2)
print(s.age)
print(s.name)
print(s.gender)
print(s.aaa)

#查看mro顺序
print(Son.mro())
print(Son.__mro__)
print(Father.__mro__)

print('*'*10)

'''
多层多继承时，方法的查找顺序也遵循mro
'''
class A(object):
    def show(self):
        print('A_show  run...')

class B(A):
    pass

class C(A):
    def show(self):
        #仍然想在C中调用A的方法，可以采用super（） 或者直接用类名调用
        super().show()  #找所在类中的下一个类进行初始化，按照mro顺序进行查找
        # A.show(self) #注意给参数self
        print('C_show  run...')

class D(B,C):
    # def show(self):
    #     print('D_show  run...')
    pass


#测试
d=D()
d.show()