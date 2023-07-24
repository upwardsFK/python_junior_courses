'''
异常处理
'''
s='hello'
# print(s.find('O'))  #find 如果没有查找到，返回-1


#此时这句代码就会出现异常，继续异常处理
try:
    print(s.index('O'))  #index 查不到就报错
except ValueError:   #如果不确定到底是那种错误，就写其父类Exception
    print('未查找到该字符')
#使用try来尝试运行后面语句块中的代码，如果从代码发生异常问题
#那么异常信息就会被except所捕捉，进而运行except后面的代码，来进行异常处理
#如果程序正常进行，说明错误信息没有出来，进而捕捉不到，因此except后面的代码不会被运行
print('pp')

'''
异常传递
'''
def Fun_a():
    print('FUN.A RUN...')
    Fun_b()

def Fun_b():
    print('FUN.B RUN...')
    Fun_c()

def Fun_c():
    print('FUN.C RUN...')
    try:
        print(1/0)
    except:
        print('你的除数为0了')

Fun_a()
#Traceback (most recent call last):
  #File "C:/Users/86150/PycharmProjects/pythonProject/p_10.py", line 33, in <module>
#     Fun_a()
#   File "C:/Users/86150/PycharmProjects/pythonProject/p_10.py", line 23, in Fun_a
#     Fun_b()
#   File "C:/Users/86150/PycharmProjects/pythonProject/p_10.py", line 27, in Fun_b
#     Fun_c()
#   File "C:/Users/86150/PycharmProjects/pythonProject/p_10.py", line 31, in Fun_c
#     print(1/0)
# ZeroDivisionError: division by zero

'''
多异常的处理
'''
# 同时捕捉多个异常，但同一时刻只能有一个异常发生
# try:
#     n/0
# except(NameError,ZeroDivisionError) as e:  #用小括号元组的形式将多个异常错误进行包装
#     print('出错了',e)

'''
异常处理子句，else
'''
# try:
#     f=open('a.txt','r')
# except Exception as e:
#     print('要打开的文件不存在')
#     print(e)
# else:
#     print(f.read())
# finally:
#     #finally 中的内容，不管是否出现异常，都要进行执行
#     #一般这个模块中，写的内容都是资源的关闭和回收
#     #例如：文件的关闭，网络连接的关闭，数据库的关闭
#     f.close()


'''
自定义异常类
'''

#定义一个用来判断电话号码是不是全部是数字的错误类型
class IphoneNumbernotdigitError(Exception):
    pass

#定义一个用来手机号长度是否合法的异常
class IphoneNumberlengthError(Exception):  #IphoneNumbernotdigitError='电话号码位数不正确'
    def __init__(self,msg):
        self.__msg=msg

    def __str__(self):
        return self.__msg

#定义一个函数，用来获取电话号码
def get_phonenumber():
    pn=input('请输入11位的电话号码')
    if pn.isdigit()==False:  #即输入的电话号码不为全数字
        #此时抛出电话号码不适全数字的错误类型
        raise IphoneNumbernotdigitError()  #raise类名（）
    elif len(pn)!=11:
        raise IphoneNumberlengthError('电话号码位数不正确')
    else:
        return pn+'电话号码输入正确'