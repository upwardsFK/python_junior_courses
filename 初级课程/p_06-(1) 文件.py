# file=open('a.txt','r')
# # while True:
# #     a=file.read(1)
# #     print(a,end='')
# #     if a=='' :
# #         break
#
# '''
# 文档其他读取方式
# '''
# a = file.readlines()
# print(a)
# for i in a:
#     print(i,end='')
#
# file.close()

'''
文档其他操作
os 模块
rename()
remove()
mkdir()
getcwd()
chdir()
listdir() 掌握
rmdir()
'''

import os
# # # os.mkdir('fk')#make directory 创建一个目录
# # print(os.getcwd())#get current work directory 获取当前工作目录
#listdir 获取当前目录下的全部文件
a= os.listdir('.')
for i in a:
    print(i)



# '''
# 实现文件复制
# '''
#
# def copy_test(jiu,xin):
#     c = open(jiu, 'r')
#     d = open(xin, 'w')
#     # jiu的读取出来,加入到xin的里面
#     while True:
#         a = c.read(1024)
#         if a == '':
#             print("拷贝成功")
#             break
#         d.write(a)
#     c.close()
#     d.close()
#
# copy_test('e.txt','a.txt')