num = int(input('請輸入要存幾筆資料'))
a = {}
for i in range(num):
    key = input('請輸入名稱')
    value = input('請輸入資料')
    a[key] = value
    print(a)

r = input('請輸入要移除的資料')
a.pop(r, "")
print(a)

for key, value in a.items():
    print(key + ":" + value)

f = input("請輸入想輸入的資料")
print(f in a)
