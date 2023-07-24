'''
私有属性
'''
# class Account(object):
#     def __init__(self,name,balance):
#         #定义了两个公有属性
#         self.name=name
#         self.balance=balance
#
# #实例对象
# Tom=Account('Tom',99999)
# #在class外部直接访问class内部的信息，不安全
# print(Tom.name)
# print(Tom.balance)

#当一个类中的属性和方法全部是私有的时候，该类无意义
class Account(object):
    def __init__(self,name,balance):
        #定义了两个私有属性
        self.__name=name
        self.__balance=balance
    #私有属性定义好后，可以保证数据的安全
    #但是还有需求对属性进行访问，可以通过公有的接口方法进行访问
    #一般对私有属性提供一种叫存取器方法的公有方法
    #set/get方法
    #set_属性名  get_属性名

    #定义存取器的公有方法

    #名字不可更改，直接获取名字即可
    def get_name(self):   #get_私有属性名
        return self.__name
    #余额会更改,需要定义存和取
    #先定义存
    def set_balance(self,balance):  #set_私有属性名
        if isinstance(balance,int):
            self.__balance=balance
        else:
            print("不要存冥币")
    #再定义取，并全部取出
    def get_all_balance(self):
        return self.__balance




#实例对象
Tom=Account('Tom',0)

# #测试私有属性在class外部是不是可以访问的，系统报错:
# #AttributeError: 'Account' object has no attribute '__name'
# print(Tom.__name,Tom.__balance)
print(Tom.get_name())
Tom.set_balance(10000)
print(Tom.get_all_balance())



