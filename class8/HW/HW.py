c = int(input("請輸入開始數字"))
a = int(input("請輸入結束數字"))
s = " "
for x in range(c, a + 1):
    s = 2
    while x % s != 0 and c < x + 1:
        s += 1

    if x == s:
        print(x)
