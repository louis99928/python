# import os

# file_path = "class7\\HW\\HW.py"  # 檔案路徑

# if os.path.isfile(file_path):
#     print("檔案存在")
# else:
#     print("檔案不存在")

#1. 要開啟的檔名
fileName = "test.txt"
#2. 指定w/ r /a mode
Mode = "r"
#3. 開啟檔案
myFile = open(fileName, Mode)
#4. 寫入檔案 \n 換行符號
n = myFile.read()
print(n)
#5. 關閉檔案
myFile.close()
