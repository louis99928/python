n = int(input("請輸入正整數"))
a = 1

for i in range(1, (n // 7) + 2):
    c = (3 * (a * 2 - 1))
    if c <= n:
        print(c)
    c = (3 * (a * 2))
    if c <= n:
        print(c)
    c = (7 * a)
    if c <= n:
        print(c)
    a = a + 1
