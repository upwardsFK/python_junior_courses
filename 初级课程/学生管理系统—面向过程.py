'''
学生管理系统
首先显示操作流程
 a.录入学生信息（学生信息包括学号，姓名，年龄，用字典保存），所有的学生信息用列表保存
 a.查询学生信息
 c.删除学生信息
 d.更改学生信息
 e.显示所有学生信息
 f.退出系统
'''



#定义一个主函数
def main():
    #提供死循环
    while True:
    #先打印功能字母进行提示
     show()
     a=input("请输入功能字母")
     if a=='a':
          luru()
     elif a=='b':
         chaxunxuehao=input("请输入你要查找学生的学号")
         chaxun(chaxunxuehao)
     elif a=='c':
         shanchuxuehao=input("请输入你要删除的学生的学号")
         shanchu(shanchuxuehao)
     elif a=='d':
         genggaixuehao=input("请输入你要更改的学生的学号")
         genggai(genggaixuehao)
     elif a=='e':
         xianshiall()
     elif a=='f':
         exit(0)
     else:
         print("输入功能字母错误")

def show():
    print("a.录入学生信息, b.查询学生信息,c.删除学生信息,d.更改学生信息,e.显示所有的学生信息，f.退出系统")

#录入学生信息
student_list=[]
def luru():
    student_dict={}
    student_dict['学号']=  input("请输入录入学生的学号")
    student_dict['姓名'] = input("请输入录入学生的姓名")
    student_dict['年龄'] = input("请输入录入学生的年龄")
    student_list.append(student_dict)

#开始进行查询
def chaxun(chaxunxuehao):
    for i in student_list:
        if i['学号']==chaxunxuehao:
            print("学号：%s" % i['学号'], "姓名：%s" % i['姓名'], "年龄:%s" % i['年龄'])
            return i
    else:
        print("该生不存在")


#开始进行删除
def shanchu(shanchuxuehao):
    #先查找
    a=chaxun(shanchuxuehao)
    if a!= None:
        student_list.remove(a)
        print("删除成功")

def genggai(genggaixuehao):
    for i in student_list:
        for a in i:
            if i[a]==genggaixuehao:
                i['学号']=  input("成功，请输入修改后的学生学号")
                i['姓名'] = input("请输入修改后的学生姓名")
                i['年龄'] = input("请输入修改后的学生年龄")
                print("修改成功")


def xianshiall():
     for i in student_list:
         for a in i:
             print(f'{a}:{i[a]}',end=' ')
         print()



main()