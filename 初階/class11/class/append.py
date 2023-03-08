bag = []
size = int(input("請輸入背包大小"))
for i in range(size):
    t = input("請輸入想裝的東西")
    bag.append(t)
    print(bag)

q = (bag.count(bag))

bag2 = []
for i in bag:
    if not (i in bag2):
        bag2.append(i)
        print(f'{i}={bag.count(i)}')

# r = input("請輸入你想要移除的東西")
# while r in bag:
#     bag.remove(r)

# print(bag)

# c = input("請輸入想計算的東西")
# print(bag.count(c))