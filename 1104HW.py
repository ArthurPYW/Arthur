"""
@HW_Due20201104~1108
1.print輸出以下規律文字(鋸齒圖)內容
2.輸出成txt/csv/xlcs 等外部文件
3.prinit出外部文件位址

(請把底線改成空白, 底線只是方便辨識)
_____*****
____*****
___*****
__*****
_*****
*****
_*****
__*****
___*****
____*****
_____*****
"""
#待優化, 已可以輸出字串by print; 需新增STR + append as newSTR and Out as file
import numpy as np #適用array
import os #讀取檔案等套件
f = open("test.txt","w") #w為覆寫, 打開特定文件覆寫下面內容

algoIndex = 0
algoStr = ""
algoStrLoop = ""
algoStrIndex = int(input("Input your star count(1~10):"))
#algoEmpIndex = int(input("Input your Empty count(1~10):"))
algoIndex = int(input("Input your lucky number(1~10):")) #空白數量

for y in range(algoStrIndex):
    algoStrLoop = algoStrLoop + "*"
    #決定你的星星數量, 並固定他as STR
#print(algoStrLoop)#test
#print(algoStrIndex)#test
i = algoIndex #用作下半部測試
z = algoIndex #用作上半度測試
b = algoIndex #備用測試

for c in range (b) : #c從0,1,2~b
    #print('testloop,c:',c,' z:',z)#測試從0開始但希望倒裝
    z = b - c #倒裝
    for a in range(z) :
        print('_',end = '', file = f)
        z -= 1
    print(algoStrLoop, file = f) #空白+星星
    c -= 1

for i in range(algoIndex + 1) : #input數字會影響這個迴圈走幾次
    #print(np.repeat('',algoIndex)) #適用array
    #algoStr = ""
    for x in range(i) :
        print('_',end ='', file = f)
    print(algoStrLoop, file = f)

#print("這是要寫入的資料\n", file = f)
#print("這是第二行資料\n", file = f)
f.close()#寫入資料結束

with open("test.txt", "r") as g :#打開特定資料名稱
    data = g.read()#讀取此檔案
    print(data)#print檔案
print(os.getcwd())#獲取當前路徑
#參考檔案位址網站https://www.itread01.com/content/1542890347.html