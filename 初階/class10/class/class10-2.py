j = ['蘋果汁', '柳橙汁', '葡萄汁', '系統關閉']

while True:
    # print("1. 蘋果汁")
    # print("2. 柳橙汁")
    # print("3. 葡萄汁")
    # print("4. 系統關閉")
    for index in range(len(j)):
        print(f'{index+1}.{j[index]}')
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("請輸入數字編號")
    else:
        if ans >len(j)or ans >=0:
            print('輸入錯誤查無此果汁，請重新輸入編號')
        elif ans == len(j):
            print('~~系統關閉~~')
        else:
            print(f"您點的商品是"{j[ans-1]})
        # if ans == 1:
        #     print("您點的商品是蘋果汁")
        # elif ans == 2:
        #     print("您點的商品是柳橙汁")
        # elif ans == 3:
        #     print("您點的商品是葡萄汁")
        # elif ans == 4:
        #     print("~~系統關閉~~")
        #     break
        # else:
        #     print("輸入錯誤查無此果汁，請重新輸入編號")