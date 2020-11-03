# Write your code here :-)
#20201103#
#加設 四戰三勝
#當玩家一勝後, 電腦贏的機率變成50%;  玩家兩勝後, 電腦贏的機率變70%
# #=註解
#var
Game_001_Start_str = "This is 10/30 HomeWork"

#可優化, 新增局數, 修正變數名稱, 修改不必要回圈, 修改概率STR
import random
import numpy as np
WinWord = "You  win  "
LoseWording = "You Lost?"
noWnoL = "Drew?"
WinIndex = 0
gameIndex = 0
AnsString = "SRPSRPSRP"
DraftArrayW50 = [0,0,1,2]
DraftArraW70 = [0,0,0,0,0,0,0,1,1,2]

while WinIndex <= 3 and gameIndex < 4:
    InAn_01 = str(input("You chose (S/R/P)?: "))
    gameIndex += 1
    if WinIndex == 0 :
        CompeAns_001 = random.choice("SRP")
        print("W0 random test")
    elif WinIndex == 1 :
        cheatIndex = random.choice(DraftArrayW50)
        print("W1")
        print("cheatIndex:",cheatIndex)
        CompeAns_001 = AnsString[cheatIndex + AnsString.find(InAn_01.upper()) +1]
        print("cheatIndex:",cheatIndex,"ComAns",CompeAns_001)
    elif WinIndex == 2 :
        print("W2")
        cheatIndex = random.choice(DraftArraW70)
        print("cheatIndex:",cheatIndex)
        CompeAns_001 = AnsString[cheatIndex + AnsString.find(InAn_01.upper()) +1]
        print("cheatIndex:",cheatIndex,"ComAns",CompeAns_001)
    else:
        break
    #猜拳判斷迴圈
    if InAn_01.upper() == "S" and CompeAns_001 == "P":
        WinIndex += 1
        print("Win, it just have",CompeAns_001,"You show",InAn_01.upper(),WinWord,"你已經勝:",WinIndex,'\n','目前第',gameIndex,'局')
    elif InAn_01.upper() == "R" and CompeAns_001 == "S":
        WinIndex += 1
        print("Win, it just have",CompeAns_001,"You show",InAn_01.upper(),WinWord,"你已經勝:",WinIndex,'\n','目前第',gameIndex,'局')
    elif InAn_01.upper() == "P" and CompeAns_001 =="R":
        WinIndex += 1
        print("Win, it just have",CompeAns_001,"You show",InAn_01.upper(),WinWord,"你已經勝:",WinIndex,'\n','目前第',gameIndex,'局')
    elif InAn_01.upper() == CompeAns_001.upper():
        print("平手","its answer:",CompeAns_001," and your is :",InAn_01.upper(),'\n','目前第',gameIndex,'局')
    else :
        print("LostGame","its answer:",CompeAns_001," and your is :",InAn_01.upper(),'\n','目前第',gameIndex,'局')

print('\n',"EndTest")