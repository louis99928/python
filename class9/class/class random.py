import random as r

# try:
#     ans_num = int(input('請猜一個1-100的數字'))
# except:
#     print("input error!!")

# o = r.randrange(10)
# print(o)
s = 1
b = 100
m = 0
a = r.randint(1, 100)
while m != a:
    m = int(input('請猜一個' + s + '到' + b + '的數字'))
    if m < a:
        print('大一點')
    elif m > a:
        print('小一點')

print('恭喜答對')
