def test_card():
    dict={}
    dict['姓名']=input("请输入你的姓名")
    dict['年龄']=input("请输入你的年龄")
    dict['地址']=input("请输入你的地址")
    return dict

def show(card):
    for i in card:
        print(i,card[i])

show(test_card())