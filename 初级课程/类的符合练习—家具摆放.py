#先创建一个家具类，有属性：名字与占地面积
class Furniture(object):
    #用init方法，绑定属性：名字与面积
    def __init__(self,name,area):
        self.name=name
        self.area=area
    #用str()规定输出格式
    def __str__(self):
        s=f'{self.name}  占用了{self.area}平方米'
        return s

#再创建一个房子类，有属性：地址与面积
class House(object):
    #用init方法，绑定属性：地址与面积
    def __init__(self,address,area):
        self.address=address
        self.area=area
        self.free_area= area * 0.3
        self.House_furniture=[]
    #添加加入家具的方法
    def add_furniture(self,fur):
        if fur.area<self.free_area:
            self.House_furniture.append(fur)
            self.free_area=self.free_area-fur.area
            print(f'添加了{str(fur)},还剩余{self.free_area}平方米')
        else:
            print("空间不足，加入此家具失败")

    #用str()规定输出格式
    def __str__(self):
        a = f'在{self.address}的房子占用了{self.area}平方米\n'+'家具有：\n'
        if len(self.House_furniture)==0:
            t=a+'新房子，无家具'
            return t
        else:
            for i in self.House_furniture:
                a+=str(i)+'\n'
            return a


#测试
home=House('裕翔街26号',150)


desk=Furniture('桌子',5)
home.add_furniture(desk)   # = home.add_furniture(Furniture('桌子',5))
home.add_furniture(Furniture('椅子',5))
print(home)