bag = {}
e = 0
while True:
    print('1.新增科目')
    print('2.移除成績')
    print('3.關閉系統')
    print('4.算平均')
    num = input('請輸入功能')
    if num == '1':
        key = input('請輸入科目')
        value = int(input('請輸入成績'))
        bag[key] = value
    elif num == '2':
        r = input('請輸入要移除的科木與成績')
        bag.pop(r, "")
    elif num == '3':
        break
    elif num == '4':
        for i in bag.values():
            e = e + i

        print('你的平均是:', e / len(bag))

    else:
        print('')
    items = bag.items()
    for key, value in items:
        print(key + ":", value)

# num = int(input('請輸入要存幾筆資料'))
# a = {}
# for i in range(num):
#     key = input('請輸入名稱')
#     value = input('請輸入資料')
#     a[key] = value
#     print(a)

# r = input('請輸入要移除的資料')
# a.pop(r, "")
# print(a)

# for key, value in a.items():
#     print(key + ":" + value)

# f = input("請輸入想輸入的資料")
# print(f in a)
