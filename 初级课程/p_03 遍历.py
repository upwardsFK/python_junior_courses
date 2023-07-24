# '''
# 12345
# '''
# s=input("输入")
# len=len(s)
# for i in range(len):
#     a=s[i]
#     print(a)

# i=1
# while i<=9:
#     j=1
#     while j<=9:
#         print("%dx%d=%d" %(i,j,i*j),end=' ')
#         if i==j:
#             break
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("*",end=' ')
#         j+=1
#     print()
#     i+=1

i=1
while i<=5:
    j=1
    while j<=5:
        print("*",end='')
        if i==j:
            break
        j+=1
    print()
    i+=1