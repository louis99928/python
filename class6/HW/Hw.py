import turtle as t

t.penup()
t.speed(0)
for i in range(1, 370, 45):
    t.forward(100)
    t.stamp()
    t.home()
    t.right(i)

t.done()
