'''
批量读取文件夹下的所有源文件，改名后进行复制
'''
# import  os
#
# def copy_file(src,dst):
#     #切换路径到源文件夹下去
#     os.chdir(src)
#     #进行改名
#     #首先读取该源文件夹下的所有文件名称
#     name_file=os.listdir('.')
#     #再遍历每一个文件名
#     for i in name_file:
#         #对文件名进行分割
#         a=i.rpartition('.')  #(分割成一个元组)
#         #开始改名,修改后的名字用gaihou_name进行定义，并用下方格式进行表示
#         gaihou_name=dst+'/'+a[0]+'bak'+a[1]+a[2]
#
#         #改完名字后进行复制
#         #先分别以读，写方式打开内容（用二进制形式）
#         file_r=open('i','rb')
#         file_w=open('gaihou_name','wb')
#         #进入循环，开始复制
#         while True:
#             #注意循环结束条件
#             content=file_r.read(4096)
#             if content==a'':
#                 print(f'{i}复制成功')
#                 file_r.close()
#                 file_w.close()
#                 break
#             file_w.write(content)
#     else:
#         print(f'一共复制了{len(name_file)}个文件')
#
# src='C:\Users\86150\Desktop\pythonProject'
# dst='C:\Users\86150\Desktop\pythonProject_back'
# copy_file(src,dst)

'''
面向对象-设计一个类，类分为旧式类（经典类）和新式类
'''
# #面向对象的三大特征：封装、继承、多态
# #定义一个英雄类(使用经典类1)
# class Hero:
#     #定义一个方法
#     def skill(self):
#         print("放大招")
#
# #定义一个人类(使用经典类2)
# class Person():
#     #定义两个方法
#     def eat(self,food):
#         print("吃",food)
#
#     def sleep(self):
#         print("每天至少睡眠八小时")
#
# #定义一个狗类(采用新式类)
# class Dog(object):#加上object
#     def bark(self):
#         print('wolf,wolf....')
#
#
# '''
# 实例对象
# '''
# #先抽象一个类
# class People(object):
#     def eat(self,food):
#         print(self.name,"正在吃",food)
#
#     def sleep(self,time):
#         print(self.name,"睡了",time,"小时")
#
# #创建一个实例对象
# Tom=People()
# #创建多个实例对象
# Jack=People()
# Rose=People()
# #为实例对象动态绑定一个属性:name(在创建对象之后进行绑定)
# Tom.name='Tom'
# Jack.name='Jack'
# Rose.name='Rose'
# #让对象开始执行类中的方法
# Tom.eat('饭')
# Tom.sleep(9)
# #让多个对象开始执行类中的方法
# Jack.eat('土')
# Jack.sleep(9)
# Rose.eat('满汉全席')
# Rose.sleep(10)

'''
__init__方法
该方法会在创建实例对象时自动调用，并对该对象进行初始化操作
'''
# class Cat(object):
#     #先def实现魔法方法__init__,用此来为对象初始化属性
#     def __init__(self,name,age):
#         print("init RUN...",self)
#         #绑定属性时，用self.属性名=值 进行定义
#         self.name=name
#         self.age=age
#     def show(self):
#         print(self.name,self.age)
#
#
# #开始创建实例对象
# tom=Cat('Tom',1)
#
# #使用类中的方法
# #在调用方法时，方法的第一个参数self不用手动传
# #这个参数会由解释器自动将使用该方法的对象传进去
# tom.show()#即tom=self

'''
__str__ 方法
使用场景：1.通过print（）函数打印时，会自动调用该方法 
        2.通过str（）方法对自定义的对象进行转换时，会自动调用该方法
'''
# class Cat(object):
#     def __init__(self,name,age,height):
#         self.username=name
#         self.userage=age
#         self.userheight=height   #此时有三个属性，username、userage、userheight
#     #实现__str__ 方法,此方法必须有返回值，且返回值必须为字符串，空串也行
#     def __str__(self):
#         print("str RUN",self.username)
#         #如果需要将对象的属性按照一定格式输出，可以在这里进行格式修饰
#         #修饰完后，让这个修饰后的字符串返回，让str()方法执行时，得到格式修饰后的字符串
#         s=self.username.ljust(10)+str(self.userage).ljust(5)+self.userheight.ljust(5)
#         return s
#
# tom=Cat('Tom',1,'50cm')
# print(tom) #默认没有实现__str__ 方法，打印出的格式为：<模块名.类名 object at 地址>
#            #如果想要按自己想要的格式输出，需要在类中实现__str__ 方法
#
# print('/'+str(tom)+'/')



'''
__del__ 方法
'''