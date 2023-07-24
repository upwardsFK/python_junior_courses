'''
自定义模块
'''


n=1
def show():
    print('aaa')

class Cat(object):
    def show(self):
        print('naa')


# #通过__all__可以改变from——import的导入规则
# __all__=['_y','__z']  #列表形式，有字符串表示
# n=1  #全局变量，模块间的公有变量
# _y=2  #私有变量，文件内私有变量
# __z=3  #私有变量，一般在类中使用，不在模块中定义


#在当前文件下测试成员的使用
print(__name__)
print(n)
show()
Cat().show()