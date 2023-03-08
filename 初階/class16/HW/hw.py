import turtle as t


def haha():
    y = int(input('請輸入Y座標'))
    x = int(input('請輸入X座標'))
    t.forward(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.left(135)
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(135)
    t.forward(50)
    t.right(90)
    t.forward(100)

    t.done()


haha()
