'''
这是一个学生模块，用来实现学生类的创建
模块中还要储存学生的信息
'''

class Student():
    def __init__(self,stu_id,stu_name,stu_age):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.stu_age=stu_age

    def __str__(self):
        return '|'+self.stu_id.ljust(5)+self.stu_name.ljust(10)+self.stu_age.ljust(3)+'|'


if __name__ == '__main__':
    tom=Student('1','Tom','12')
    print(tom)