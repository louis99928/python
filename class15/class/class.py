def hello(name):
    print(f'.....{name}')
    return f'hello {n} haha'


n = input('請輸入你的名字')
hello(n)
n1 = hello(n)
print(n1)


def my_min(a, b):
    if a < b:
        return a
    else:
        return b


x = my_min(1, 2)
print("my_min:", x)
