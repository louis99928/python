import random as r


def roll_dice(x):
    l = []
    for i in range(x):
        l.append(r.randint(1, 6))
    return l


n = int(input("請輸入擲骰子的次數:"))
n1 = roll_dice(n)
print(n1)
print(f"加總={sum(n1)}")