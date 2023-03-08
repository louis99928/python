a = int(input("請輸入大小"))
for i in range(1, a + 1):
    print(" " * (a + 1 - i) + "*" * (i + i - 1))
for b in range(1, a + 1):
    print(" " * a + "*")
