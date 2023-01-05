def exit(b):
    print(f"平均是{sum(b.values())/len(b)}")


def add(b):
    key = input("請輸入科目:")
    value = int(input("請輸入成績:"))
    b[key] = value


def delete(b):
    r = input("請輸入想刪除的key:")
    b.pop(r, "")
    print(b)


def modify(b):
    pass


b = {}
s = [add, delete, modify, exit]
while True:
    for key, value in b.items():
        print(key + ":", value)
    print("1. 新增成績")
    print("2. 刪除成績")
    print("3. 離開系統")
    ans = int(input("請輸入功能選項:"))
    s[ans - 1](b)
    if ans == len(s):
        break