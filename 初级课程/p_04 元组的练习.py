'''
元组的定义
'''
# a=(1,2,'helloword','esaa')
# print(a)
# print(type(a))
#
# i=(1,2,3,4,5,6,'hellp')
# print(len(i))
# for a in range(len(i)):
#     print(i[a])

'''
元组的嵌套和遍历
'''
# t=(1,2,6,7,8,('k',1,2,3))
# for v in t:
#     if isinstance(v,tuple):
#        for j in v:
#             print(j)
#     else:
#         print(v)

# s=[1,2,3,4,5,6,'helloworld',(1,2,3,'hello'),['hellowpd',1,5,6]]
# for i in s:
#     if isinstance(i,tuple) or isinstance(i,list):
#         for j in i:
#             print(j)
#     else:
#         print(i)


# s='abv'
# a=list(s)
# print(a)
# a[0]=
# print(a)
'''
列表的倒序
'''

s=['a','iheoslkm',1,2,3,4,5,6,798,9]
i=len(s)-1
while i>=0:
    l=[]
    a=l.append(s[i])
    i-=1
    print(a)