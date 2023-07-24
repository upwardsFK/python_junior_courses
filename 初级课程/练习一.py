'''
有四个数字1，2，3，4，能组成多少个互不相同且无重复的三位数字，各是多少
'''

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 print(str(i)+str(j)+str(k))

'''
求出100以内的所有素数
'''
# for i in range(2,101):
#     #for-else循环语句，并当迭代的对象迭代完成后仍为空时，执行else
#     # 如果在for循环中含有break时，则直接终止循环，并不会执行子句else
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

'''
求三位数的水仙花数
'''
# for i in range(100,1001):
#     s=str(i)
#     a=s[0]
#     b=s[1]
#     c=s[2]
#     if (eval(a)**3)+(eval(b)**3)+(eval(c)**3)==i:
#         print(i)

'''
输入若干数字，当输入quit退出，并计算输入数字的最大值，最小值，总和，平均值
'''
list=[]
while True:
    n=input('请输入数字，输入quit退出')
    if n=='quit':
        print('退出成功，并继续为你计算输入数字的最大值，最小值，总和，平均值')
        break
    elif n.isdigit():
        list.append(n)
    else:
        print('输入数字格式错误')
sum=0
for i in list:
    eval_i=eval(i)
    sum += eval_i
length = len(list)
average = sum / length
print(f'平均值为{average}')
print(f'总和为{sum}')

max=eval(list[0])
min=eval(list[0])
for i in list:
    eval_i=eval(i)
    if eval_i>max:
        max=eval_i
    if eval_i < min:
        min = eval_i
print(f'最大值为{max}')
print(f'最小值为{min}')




