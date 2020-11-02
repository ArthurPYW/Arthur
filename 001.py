# Write your code here :-)
#20201102#
#加設 四戰三勝
#當玩家一勝後, 電腦贏的機率變成50%;  玩家兩勝後, 電腦贏的機率變70%
# #=註解
#var
Game_001_Start_str = "This is 10/30 HomeWork"

#可優化, 雛形
import random
import numpy as np
WinnerWording = "You  win  "
LoseWording = "You Lost?"
noWnoL = "Drew?"
PlayerWinnerIndex = 0
AnsString = "SRPRPS"
DraftArrayW50 = [0,0,-1,-2]
DraftArraW70 = [0,0,0,0,0,0,0,-1,-2,-2]

Adv_001 = str(input("Time to guess(Y/N):"))
while Adv_001.upper() != "END" and PlayerWinnerIndex <= 3:
    if Adv_001.upper() == "Y" :
        if PlayerWinnerIndex == 3:
            break
        InputAns_001 = str(input("You chose (S/R/P)?: "))
        #print(AnsString.find(InputAns_001.upper())) #測試String/Array 找目標
        #print(AnsString[5])#測試STR位子

        if PlayerWinnerIndex == 0 :
            CompeAns_001 = random.choice("SRP")
            print("W0 random test")
        elif PlayerWinnerIndex == 1 :
            test00 = random.choice(DraftArrayW50)
            print("W1")
            print("test00:",test00)
            CompeAns_001 = AnsString[test00 + AnsString.find(InputAns_001.upper()) +3]
            print("test00:",test00,"ComAns",CompeAns_001)

        elif PlayerWinnerIndex == 2 :
            print("W2")
            test00 = random.choice(DraftArraW70)
            print("test00:",test00)
            CompeAns_001 = AnsString[test00 + AnsString.find(InputAns_001.upper()) +3]
            print("test00:",test00,"ComAns",CompeAns_001)
        else:
            break
        if InputAns_001.upper() == "S" and CompeAns_001 == "P":
            PlayerWinnerIndex += 1
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,"你勝:",PlayerWinnerIndex,'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        elif InputAns_001.upper() == "R" and CompeAns_001 == "S":
            PlayerWinnerIndex += 1
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,"你勝:",PlayerWinnerIndex,'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        elif InputAns_001.upper() == "P" and CompeAns_001 =="R":
            PlayerWinnerIndex += 1
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,"你勝:",PlayerWinnerIndex,'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        elif InputAns_001.upper() == CompeAns_001.upper():
            print("平手","its answer:",CompeAns_001," and your is :",InputAns_001.upper(),'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        else :
            print("LostGame","its answer:",CompeAns_001," and your is :",InputAns_001.upper(),'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
            #break
    elif Adv_001.upper() == "N":#對方不開始遊戲時候
        print("what a pity, you don't start yet, time to END")
        break
    #elif Adv_001.upper() == "END":
        #print("you get it, see u")
        #break
    else :
        print("修理ing")
        break

print('\n',"EndTest")


"""
#雛形
GameStart = str(input("Game Start (Y/N):"))
#def Gmae_001 (GameStart) :
#def Game(GameStart) :
while GameStart != "test":
        if GameStart.upper() == "Y":
            print("Game Start already")
            GameStart = "c"
        elif GameStart.upper() == "N":
            print("Allright, game over")
            GameStart = "Y"
        else:
            print("Not answer")
            break
"""


"""
#導入Recursive_001
GameRe_000 = 0 #測試用
GameRe_001 = str(input("Game Start (Y/N):"))#讓UX餵答案近來
n = 0
#del Game1(n): #新增判斷變數並加入func
if n == 0 and GameRe_001.upper() == "Y":
    GameRe_002 = str(input("What's your choise(S/P/R):"))
    if GameRe_002.upper() == "S" or "P" or "R" :
        print("Your compe show S, you lose")
    n = 1
elif n == 0 and GameRe_001.upper() == "N":
    print("It's time to end ")
else :  #n != 0 or string != Y/N
    print("input incorrect answer")
    GameRe_001 = str(input("Game Start (Y/N):"))
    #GameRe_001 = "Y"
    n=1
"""