"""
Topic:請使用input and print打造對話機器人
​
e.g.
old = input("How old are you?")
print("I am " + old)
​
1.Show:How old are you?
2.input:12
3.Output:I am 12
"""

import time
import random as r

print('hi')
time.sleep(2)
name = input('請問你的名子是什麼?')
print('你好' + name)
hobbies = input('你喜歡做什麼?')
time.sleep(2)
print('我也喜歡' + hobbies)
time.sleep(1)
friend = None
while friend != '要':
    friend = input('要不要跟我聊天?填入要或不要')
    if friend == '要':
        print('好')
    elif friend == '不要':
        print("為什麼?")
        time.sleep(1)
        print('拜託拜託拜託')
    else:
        print('我不知道你在說什麼')
        time.sleep(2)
print('我們來玩猜數字遊戲吧!')

ans_num = 0
sec_num = r.randint(1, 100)
while ans_num != sec_num:
    try:
        ans_num = int(input('請猜一個1-100的數字'))
    except:
        print("input error!!")
    else:
        if ans_num < sec_num:
            print('大一點')
        elif ans_num > sec_num:
            print('小一點')

print('恭喜答對')
