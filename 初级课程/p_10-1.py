'''
类方法
'''
#定义一个类
class Math(object):
    #定义一个类属性
    n=999
    #定义一个类方法,需要先@classmethod一下
    @classmethod  #这是一个装饰器，用来表示下面的方法是类方法
    def info(cls):  #自动传入cls, cls为类对象
        print(cls.n)
    #再定义一个求和的类方法
    @classmethod
    def sum(cls,*args):
        m=0
        for i in args:
            m=m+i
        return m


#用类对象（类名）来调用类方法
Math.info()  #info(Math)
# print(Math.sum(1, 2, 3, 4, 5))


'''
静态方法
'''
# #创建一个编码类
# class Unicode(object):
#     #编码方法
#     @staticmethod #以静态方法让下面的函数为正常函数，往里传入仅仅需要的参数
#     def unicode_data(data,format):
#         print(f'数据{data}使用{format}格式编码成功')
#     #解码方法
#     @staticmethod
#     def deunicode_data(data,format):
#         print(f'数据{data}使用{format}格式解码成功')
#
# #实例一个对象
# # uc=Unicode()
# #通过一个实例对象调用unicode_data方法
# # uc.unicode_data('a','utf_8')   #此时括号内有三个参数（uc，'a','utf_8'），但是只要求两个参数，报错
#
# #通过类来调用unicode_data方法
# Unicode.unicode_data('a','utf_8')
# Unicode.deunicode_data('456','GBK')


'''
系统模块的使用
'''
# #导入os(操作系统)模块
# import os
# #导入time模块
# import time
# print('正在为您打印当前工作目录')
# time.sleep(5) #sleep函数是time模块中定义的函数，用来让程序休眠，这是一个阻塞函数
# print(os.getcwd())

'''
模块导入的两种方式以及别名
'''
'''
方式一
'''
# import p_10自定义模块
# #调用模块中的全局变量
# print(p_10自定义模块.n)
# #调用模块中的show()
# p_10自定义模块.show()
# #调用模块中的类
# #先实例一个对象,一般格式为tom=Cat(),但在这里仍然需要强调一下是p_10自定义模块中的Cat()类
# #因此格式为
# tom=p_10自定义模块.Cat()
# #调用Cat()类中的show()方法,找到了tom所在的Cat()位置,自然就能找到tom所在Cat()类下的方法并执行
# tom.show()

'''
方式一的别名形式
'''
# import p_10自定义模块 as p
# print(p.n)
# p.Cat().show() #此时的p.Cat()为匿名对象,只能使用一次

'''
方式二
'''
#采用from——import方式导入成员，这种模式不需要再用模块名.成员的形式
#可在当前文件中直接使用成员名，相当于将导入的成员复制到了本地一份

# from p_10自定义模块 import Cat as C
# C().show()

'''
方式三
'''
#利用from——import格式来导入模块中的全部内容，同样不需要采用模块名.成员名来调用
# from p_10自定义模块 import * #默认导入p_10自定义模块中的全部内容
#                          #使用通配符*进行导入，就不能再用as来为他起别名了
#
# print(n)
# show()
# Cat().show()

'''
两种导入模块的区别
'''
#import方式进行导入之后，没有任何限制，都可以访问
# import p_10自定义模块 as p10m
# print(p10m.n)
# print(p10m._y)
# print(p10m.__z)

#采用from——import进行访问，有权限限制，更安全
#from p_10自定义模块 import *
# print(n)
#私有的不能访问
# print(_y)  #name '_y' is not defined
# print(__z)

'''
name的使用
'''

# import p_10自定义模块


'''
使用包中的模块
'''
# #使用import方式进行导入
# import .a  #导入b包内的a模块
# print(cn.a.n)
# #使用from——import方式进行导入
# from cn import a  #从b包中引入a，此时不能直接去使用变量名，仍需要使用模块名.成员
# print(a.n)
# #使用from——import方式进行导入，不需要进行模块名调用的方式
# from cn.a import n
# print(n)

'''
__init__.py文件的使用
'''
# #采用import进行导入
# import cn.itcast.web.a as wba
#
# print(wba.n)
# #采用from——import进行导入
#
# from cn.itcast.web import a as wa
# print(wa.n)
#
# from cn.itcast.web.a import *
# print(n)

#想直接导入web包
# import cn.itcast.web as web
# print(web.a.m)
# print(web.b.n)
#
# from cn.itcast import web
# print(web.b.n)
# print(web.a.m)


#尝试__all__用法
# from cn.itcast.web import *
# print(a.m)
# print(b.n)