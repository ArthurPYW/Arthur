# Write your code here :-)
#20201027#
# #=註解
#var
a = "Hell World"
Game_001_Start_str = "This is 10/28 HomeWork"
"""
weahter = "sunny"
if weahter == rainy :
    print("yoyo")
    else:
        print("non yoyo")
"""

"""
#Sample If and else with input
score = int(input("score:"))
if score >= 60:
    print("成績及格!")
else:
    print("不及格，被當了!")
"""

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

#導入002
import random
WinnerWording = "You just win the game"
LoseWording = "You almost win, trt again?"
noWnoL = "Well, it has same answer with you, try again?"

Adv_001 = str(input("Time to guess(Y/N):"))
while Adv_001.upper() != "END":
    if Adv_001.upper() == "Y":
        InputAns_001 = str(input("You chose (S/R/P)?: "))
        CompeAns_001 = random.choice("SRP")
        if InputAns_001.upper() == "S" and CompeAns_001 == "P":
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        elif InputAns_001.upper() == "R" and CompeAns_001 == "S":
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,'\n')
            InpuAns_try = str(input("Wanna Try?(Y/N):"))
            if InpuAns_try.upper() == "N":
               break
        elif InputAns_001.upper() == "P" and CompeAns_001 =="R":
            print("Win, it just have",CompeAns_001,"You show",InputAns_001.upper(),WinnerWording,'\n')
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
            break
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