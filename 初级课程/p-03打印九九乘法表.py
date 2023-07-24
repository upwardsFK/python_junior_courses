'''
打印九九乘法表
'''
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print("%d*%d=%-3d" %(j,i,i*j),end=' ')
#         j+=1
#     print()
#     i+=1
def hanshu():

    i=1
    while i<=9:
        j=1
        while j<=9:
            print("%d*%d=%-3d" %(j,i,i*j),end=' ')
            if i==j:
                break
            j+=1
        print()
        i+=1



hanshu()
