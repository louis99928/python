import turtle as t
import time
for i in range(1, 360, 6):
    t.forward(100)
    time.sleep(1)
    t.home()
    t.clear()
    t.right(i)

t.done
