s = 2
a = float(input("請輸入數字"))

while a % s != 0 and s < a + 1:
    s += 1

if s == a:
    print("yes")
else:
    print("no")
