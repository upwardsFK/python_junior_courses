'''
这是一个学生管理模块，用来对学生的信息进行管理
主要包括对学生信息的增删改查
'''


#在学生管理系统中会用到学生，需要导入学生类
from p_12学生类 import *
class Studentmanagersystem(object):
    #定义一个容器属性（空字典），用来保存所有被管理学生的信息
    #并规定格式:以学生id作为key 学生id:学生对象
    def __init__(self):
        self.students={}
        #加载数据
        self.__load_data()


    def start(self):
        print('系统启动成功')
        #进入死循环
        while True:
            #打印菜单
            self.__print_menu()
            #输入要进行执行的代号
            code=input('请输入您希望执行内容的数字代号')
            #判断code是不是数字，并判断是否是在0-5之间的数字
            if code.isdigit():
                n=eval(code)
                if n>=0 and n<=5:
                    #满足上述条件，便开始进行操作
                    self.__operator(code)
                else:
                    print('输入数字代号超出范围，请您重新输入')
            else:
                print('输入的数字代号非法，请您重新输入')


    #开始创建学生管理系统类中的各项方法——增删改查
    #先打印菜单提示
    def __print_menu(self):
        print('*'*30)
        print('欢迎使用【学生管理系统】V1.0')
        print('1.添加学生  2.显示全部学生信息  3.咨询学生  4.修改学生  5.删除学生')
        print('0.退出系统')
        print('*'*30)

    #用来执行操作，实现管理的代码逻辑
    def __operator(self,code):
        print('选择了功能'+code)
        #往后过程中，因为所给的code和四个增删改查的方法一一对应，所以考虑
        #用字典来进行存储，以code与对应的功能函数作为键值对
        stu_dict={'1':self.__add_student,
                  '2':self.__show_all,
                  '3':self.__search_student,
                  '4':self.__modify_student,
                  '5':self.__del_student,
                  '0':exit}      #方法不带（）
        #通过接收的code，来对应找到字典中的方法，并执行
        method=stu_dict[code]
        #但考虑到345需要参数，不能直接运行,加入判断
        if code=='3'or code=='4'or code=='5':
            operator_stu=input('请输入要进行操作的学生学号')
            method(operator_stu)
        elif code=='0':
            #code==0，说明要退出系统,退出前先保存数据，写入文件
            self.__save_data()
            print('已成功保存数据，并自动退出系统')
            method(0)
        else:
            method()

    #增
    def __add_student(self):
        print('开始进行添加学生')
        #获取了学生的全部信息
        stu_info=self.get_info()
        #创建一个学生对象
        stu=Student(stu_info[0],stu_info[1],stu_info[2])
        #将创建好的学生对象加到字典中，以id为key，如果id不存在，即为添加
        self.students[stu_info[0]]=stu  #存储格式：   键：学生对象

     #查
    def __search_student(self,stu_id):
        #默认没有找到
        stu=None
        if stu_id in self.students:
            stu=self.students[stu_id]
            #找到之后打印学生信息
            self.__show_singel_stu(stu)
        else:
            print(f'学号为{stu_id}的学生不存在')
        return stu

    #改
    def __modify_student(self,stu_id):
        #先找
        stu=self.__search_student(stu_id)
        if stu==None:
            print('无法修改信息')
        else:
            print('开始修改学生信息')
            #获取新数据
            new_stu_info=self.get_info()
            stu.stu_id=new_stu_info[0]
            stu.stu_name=new_stu_info[1]
            stu.stu_age=new_stu_info[2]
            print('修改成功')
            print(stu)

    #删
    def __del_student(self,stu_id):
        #先查
        stu=self.__search_student(stu_id)
        if stu==None:
            print('无法删除学生信息')
        else:
            self.students.pop(stu_id)
            print('删除成功')





    #显示单个学生的信息
    def __show_singel_stu(self,stu):
        print(stu)
    #显示所有学生的信息
    def __show_all(self):
        #遍历之后打印
        for i in self.students:
            print(self.students[i])

    #定义一个方法，用来获取学生信息
    def get_info(self):
        stu_id=input('请输入学生学号')
        stu_name=input('请输入学生姓名')
        stu_age=input('请输入学生年龄')
        return stu_id,stu_name,stu_age

    #定义其他两个方法，用来读取数据和退出程序时保存数据
    def __save_data(self):
        print('开始进行保存数据')
        #以写的方式打开一个文件
        f=open('data','w')
        #遍历所有的学生对象
        for i in self.students.values():
            #将学生对象信息转换成一个学生字符串
            stu_s=i.stu_id+' '+i.stu_name+' '+i.stu_age+'\n'
            #将已经写好的学生信息写入到打开的文件中
            f.write(stu_s)
        #写完之后关闭
        f.close()

    #加载数据
    def __load_data(self):
        print('正在为您加载数据')
        #默认file_r=None，以便finally之后进行文件的回收与销毁
        file_r=None
        try:
            file_r=open('data','r')
        except Exception as e:
            print(e,'文件不存在')
        else:
            #上边在保存数据时，每一行都保存了一个学生信息，因此需要以行读取
            content=file_r.readlines()
            #此时每一个学生信息都在content这个列表中储存
            for i in content:
                #split()默认以所有空白进行分割
                stu_info=i.split()
                #实例一个学生对象
                stu=Student(stu_info[0],stu_info[1],stu_info[2])
                #将对象传入到字典中进行储存
                self.students[stu_info[0]]=stu
        finally:
            if file_r!=None:
                file_r.close()









