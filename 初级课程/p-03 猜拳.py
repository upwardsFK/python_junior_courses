'''
a.两个角色  玩家 player  - 电脑 robot
a. 动作: 石头 0 , 剪刀 1,  布 2
c. 我的出拳: 由输入完成
d. 电脑的出拳: 随机数完成
e. 比较出拳
f. 相等 - 平局
g. 玩家赢: p0:r1  p1:r2  p2:r0
h. 剩下的情况就是电脑赢
'''
#采用非函数形式
# import random
# a=eval(input("请输入你所猜的拳"))
# a=random.randint(0,2)
# if a==a:
#     print("平局")
# elif (a==0 and a==1) or (a==1 and a==2) or (a==2 and a==0) :
#     print("玩家赢")
# else:
#     print("电脑赢")

import random
def game():
    a = eval(input("请输入你所猜的拳"))
    b=random.randint(0,2)
    if a==b:
        if (a==0 and b==0):
            return ("平局，此时你出的拳头，电脑也出的拳头")
        elif (a == 1 and b == 1):
            return ("平局，此时你出的剪刀，电脑也出的剪刀")
        else:
            return("平局，此时你出的石头，电脑也出的石头")
    elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0) :
        if (a==0 and b==1):
            return("玩家赢，此时你出的石头，电脑出的剪刀")
        elif (a==1 and b==2):
            return("玩家赢，此时你出的剪刀，电脑出的布")
        else:
            return("玩家赢，此时你出的布，电脑出的石头")
    else:
        if (a==0 and b==2):
            return ("电脑赢,此时你出的石头，电脑出的布")
        elif(a==1 and b==0):
            return ("电脑赢,此时你出的剪刀，电脑出的石头")
        else:
            return("电脑赢,此时你出的布，电脑出的剪刀")
print(game())