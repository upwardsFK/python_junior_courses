# '''
# 函数名为数据赋值给另外一个变量
# '''
#
# def show():
#     print("hello world")
#
# show()
# fuc=show
# print(fuc)
# print(show)
# fuc()
#
# '''
# 匿名函数lambda
# '''
#
# fun = lambda x:"偶数" if x%2==0 else "奇数"
# print(fun(2))


'''
高阶函数map（映射）
'''
# import math
# def kaifang(x):
#     return pow(x,2)
#
# def re_dict(my_dict):
#     dict=map(kaifang,my_dict)
#     return dict
#
# my_dict = {1, 2, 3, 4, 5, 6}
# for i in re_dict(my_dict):
#     print(i)


'''
用lambda函数进行传参
'''

# list=[1,2,3,4,5,6]
# a=map(lambda x:x**2 ,list)
# for i in a:
#     print(i)
#
# print('*'*10)

'''
高阶函数reduce
'''
# import functools
# my_list=['h','e','r']
# a=functools.reduce(lambda x,y : x.upper()+y.upper(),my_list)
# print(a)
# print('*'*10)
#
# my_list2=[i for i in range(1,6)]
# a=functools.reduce(lambda x,y:x*y,my_list2)
# print(a)


'''
高阶函数filter
'''
# my_list=['a','sbf','456','789']
# list1=filter(lambda x:x.isdigit(),my_list)
# for i in list1:
#     print(i)


'''
sort函数中的key与lambda函数
'''
list=[{'id':1,'name':'tom','age':17},{'id':3,'name':'jack','age':27},{'id':2,'name':'rose','age':97}]
list.sort(key=lambda x:x['age'],reverse=True)
print(list)

