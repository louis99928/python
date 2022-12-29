while True:
    try:
        c = float(input('請輸入華氏溫度'))
    excpt:
        print('請輸入數字')
    else:
        answer = (c - 32) * 5 / 9
        print('華氏溫度' + str(c) + ('等於攝氏溫度') + str(answer))