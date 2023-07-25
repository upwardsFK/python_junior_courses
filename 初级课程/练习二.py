'''
循环输入若干次字符，每一次只能输入一个字符，但输入quit时结束输入，并统计数字，字母，空白，其他字符各有多少
'''
# import time
# list_digit=[]
# list_alpha=[]
# list_others=[]
# list_kong=[]
# while True:
#     n=input('请输入字符，每一次只能输入一个字符,输入quit时结束输入')
#     if n=='quit':
#         break
#     elif n.isalpha():
#         list_alpha.append(n)
#     elif n.isspace():
#         list_kong.append(n)
#     elif n.isdigit():
#         list_digit.append(n)
#     else:
#         list_others.append(n)
# print('结束输入，正在为您统计数字，字母，空白，其他字符')
# time.sleep(5)
# print(f'数字的个数为{len(list_digit)}\n'
#         f'字母的个数为{len(list_alpha)}\n'
#         f'空白的个数为{len(list_kong)}\n'
#         f'其他字符的个数为{len(list_others)}')

'''
输入两个数字a,b,求s=a+aa+aaa+aaaaa+aaa...a的值
例如2，5
输出结果为2+22+222+2222+22222=24690
'''
# a=input('请输入第一个数字')
# b=eval(input('请输入第二个数字'))
# i=1
# n=0
# list=[]
# while i<b+1:
#     c=a*i
#     list.append(c)
#     i+=1
#
# d=list[n]
# while n<len(list)-1:
#     d=d+'+'+list[n+1]
#     n+=1
# eval_d=eval(d)
# print(f'{d}={eval_d}')

'''
现有姓氏和名字若干
设计函数得到一个随即名字
'''
# def hanshu():
#     import random
#     # 使用random.choice方法进行处理，前提要求为列表或者元组
#     # 创建两个列表，一个为姓，一个为名
#     last_name = ['李', '马', '孙', '冯', '王', '张']
#     first_name = ['观样', '超', '武昌', '小松', '照样']
#     l_n = random.choice(last_name)
#     f_n = random.choice(first_name)
#     return (f'生成的随机姓名为{l_n + f_n}')
#
# print(hanshu())


'''
利用随机数得到一个随机的字母和数字组成的四位验证码
然后输入看到的验证码，如果输入正确结束程序，输入错误持续输入直到正确为止
（进阶：如果输入三次不正确，更新验证码后继续）
'''
# import random
# list=[]
# for i in range(65,91):
#     alpha_higher=chr(i)
#     list.append(alpha_higher)
# for i in range(48,58):
#     number=chr(i)
#     list.append(number)
# for i in range(97,123):
#     alpha_lower=chr(i)
#     list.append(alpha_lower)

# while True:
#     n = 0
#     b = random.sample(list, 4)
#     yzm = ''.join(b)
#     print(f'得到的验证码为{yzm}')
#     while True:
#         a = input('请输入您所看到的验证码')
#         n += 1
#         if a == yzm:
#             print('输入正确，结束程序')
#             exit(0)
#         else:
#             print('输入错误请重新输入')
#             if n == 3:
#                 print('输入错误已达3次，为您更换验证码')
#                 break

'''
求出所有字符串的最小前缀
'''
#如果字符串为ab,a,abc,abd，则最小前缀为a
#如果字符串为a,abc,a,d,则没有最小前缀
#如果字符串为ab,abc,abd,abde，则最小前缀为ab
# def exer():
#     list=['abc','ab','abcd','abd','abd']
#     #对列表中的字符串按长度进行排序，找到最短串
#     list.sort(key=lambda s: len(s))
#     shortest=list[0]
#
#     for i in range(0,len(shortest)):
#         for k in list:
#             if shortest[i]!=k[i]:
#                 return shortest[:i]
#         #如果一直相等
#     return shortest
#
# print(exer())

'''
从高到低的顺序统计文章text中所有的单词使用频率
'''
#打开文件
file_r=open('a.txt','r')
#读取文件
content=file_r.read()
file_r.close()
#用任意空白进行分割，放到列表中
content_s=content.split()
#进行去重操作，用到集合
set_content=set(content_s)
#对集合遍历，搭配count函数，以字典的格式放到列表中
new_list=[]
for i in set_content:
    new_set={}
    new_set[i]=content_s.count(i)
    new_list.append(new_set)
#按照值进行逆序排序
new_list.sort(key=lambda d:list(d.values())[0],reverse=True)
print(new_list)
