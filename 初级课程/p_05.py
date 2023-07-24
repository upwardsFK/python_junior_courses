'''
列表推导式
'''
#
# c_l=[x for x in range(100)]
# print(c_l)

'''
列表推导式，带条件
'''
# c_a=[x for x in  range(100) if x%3==0]
# print(c_a)

'''
创建一个列表，列表中都是元组，且元组有两个值
'''
# c_b=[(x,y) for x in range(100)  for y in range(100)]
# print(c_b)


'''
组包和拆包
'''

# a=1,2,3,4,5
# a1,a2,a3,a4,a5=a
# print(a1)

'''
递归调用
求阶乘
'''
# def fact(a):
#     if a==1:
#         return 1
#     return a*fact(a-1)
#
# print(fact(5))



'''
global
'''

# n=0
# def hanshu():
#     global n
#     n=100
#     print(n)

'''
引用
'''


'''
默认值参数
'''
#
# def hanshu(a,a=0,v):
#     print(a,a,v)
#
# hanshu(1,2,3)


'''
不定长位置参数
'''

# def qiuhe(*args):  #args=(1,2,3)
#     s=0
#     for i in args:
#         s=s+i
#     print(s)



'''
不定长关键字参数
'''
# def hanshu(**kwargs):
#     print(kwargs)
#
#
# hanshu(n='h',m='l')



'''
可变参数的二次传递
'''

def hanshu1(a,*args,**kwargs):
    print(a)
    hanshu2(*args)#(2,3,4,5)

def hanshu2(a,b,c,d):
    print(a,b,c,d)

hanshu1(1,2,3,4,5)


'''

'''
def hanshu():
    a=1
    b=2
    c=3
    return a,b,c


print(hanshu())



