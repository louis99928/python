# password = input('請輸入密碼')
# if password == "1234":
#     print("歡迎光臨")
# elif password == "8787":
#     print('歡迎光臨')
# elif password == "1487":
#     print('歡迎光臨')
# else:
#     print('錯誤')

score = float(input('請輸入成績'))
if score >= 90:
    print('your score is A')
elif score >= 80:
    print('your score is B')
elif score >= 70:
    print('your score is C')
elif score >= 60:
    print('your score is D')
elif score < 60:
    print('your score is E')
'''
測量你的BMI值, 確認你的體重是否正常?
* BMI公式:體重(公斤) / 身高(公尺)的平方
* BMI值正常範圍:14.8到20.7之間
* BMI值過重範圍:20.7以上

EX:
請輸入身高(公尺):1.7
請輸入體重(公斤):45
你的BMI為15.570934256055365
體重過輕

請輸入身高(公尺):1.7
請輸入體重(公斤):60
你的BMI為20.761245674740486
體重正常

請輸入身高(公尺):1.7
請輸入體重(公斤):90
你的BMI為31.14186851211073
體重過重
'''