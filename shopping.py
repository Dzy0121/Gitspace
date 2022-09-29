goods = {1:'肥皂',2:'牙刷',3:'牙膏',4:'毛巾',5:'卫衣',6:'短袖',7:'长裤',8:'短裤',9:'饮料',10:'零食',11:'鞋子',12:'马自达',13:'劳斯莱斯'}
goodsKey = tuple(goods.keys())
goodsValue = list(goods.values())
money = {1: 3, 2: 5, 3: 8, 4: 5, 5: 30, 6: 20, 7: 30, 8: 20, 9: 3, 10: 6, 11: 25,12:200000,13:5000000}
face = {1:'购物',2:'结账',3:'查看余额',4:'购物清单',5:'充值'}
shop = list()
cash = 100

file = open('shopHistory.txt', 'w')
file.write('商品列表：')
file.write("\n")
for i in goodsValue:
    file.write(str(i))
    file.write(' ')
file.write("\n")

def Face():
    print(' ')
    print(face)
    print(' ')
    a = eval(input("请选择想要操作的数字："))
    if a == 1:
        Shop()
    elif a == 2:
        Pay()
    elif a == 3:
        print(' ')
        print("{}元".format(cash))
        Face()
    elif a == 4:
        Remove()
    elif a == 5:
        Cash()
    else:
        print(' ')
        print("输入错误，请重新输入:")
        Face()

def Shop():
    b = 1
    while b != 0:
        print(' ')
        print(goods)
        print(' ')
        b = eval(input("请选择你想购买的商品编号（0：退出）："))
        shop.append(goodsKey[b-1])
        continue
    shop.pop(-1)
    Face()

def Pay():
    global cash
    pay = 0
    for m in shop:
        pay = pay + money[m]
    print(' ')
    p = eval(input("{}元,是否支付（1：支付，2：返回）".format(pay)))
    if p == 1:
        if pay < cash:
            file.write('购买商品：')
            file.write("\n")
            for i in shop:
                file.write((goods[i]))
                file.write(' ')
            file.write("\n")
            print(' ')
            pa = eval(input("支付成功！是否退出（1：退出，2：返回界面）"))
            cash = cash - pay
            if pa == 1:
                print(' ')
                print("祝您生活愉快！")
            elif pa == 2:
                shop.clear()
                Face()
            else:
                print(' ')
                print("输入失败，请重新输入")
                Pay()
        elif pay >= cash:
            print(' ')
            print("余额不足，请充值")
            Face()
    elif p == 2:
        Face()
    else:
        print(' ')
        print("输入错误，请重新输入:")
        Pay()

def Cash():
    print(' ')
    c = eval(input("请输入充值金额："))
    global cash
    cash = cash + c
    print(' ')
    print("充值成功！")
    Face()

def Remove():
    for i in shop:
        print(goods[i])
    print(' ')
    s = eval(input("是否删除商品：（1：是，2：否）："))
    if s == 1:
        print(' ')
        ss = eval(input("请输入想要删除的商品编号：（0：退出）"))
        try:
            shop.remove(ss)
        except:
            print(' ')
            print("该商品不在购物车中")
            Remove()
        print(' ')
        print("删除成功！")
        Face()
    elif s == 2:
        Face()
    else:
        print(' ')
        print("输入错误，请重新输入:")
    Remove()
def main():
    print(' ')
    print("《购物车》")
    Face()
    file.close()

main()