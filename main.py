# encoding: utf-8

from time import sleep
import CropAndAnalyze
import os
from playsound import playsound
TarGoldCoin = 0 # 最小目标金币
TarExlixir = 0 # 最小目标圣水
TarDarkElixirDrill = 0 # 最小目标暗黑重油
SpoilsLoc =(100,100,450,300) # 进攻时可获取战利品的位置
NextLoc = ("2186","774") # 进攻时搜索下一个对手的按钮的坐标
EndLoc = ("210","797") # 进攻时结束战斗的坐标(目前暂时没有开发相关功能)
AccessToken = "" # 百度数字识别APIToken
def Welcome():
    print(r" __     __     ______     __         ______     ______     __    __     ______        ______   ______      ")
    print(r'/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\__  _\ /\  __ \      ')
    print(r'\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\      \/_/\ \/ \ \ \/\ \     ')
    print(r' \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\       \ \_\  \ \_____\    ')
    print(r"  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/        \/_/   \/_____/    ")
    print(r"                                                                                                            ")
    print(r' ______     ______     ______        ______     __  __     ______   ______        ______   __     __   __     _____    ')
    print(r'/\  ___\   /\  __ \   /\  ___\      /\  __ \   /\ \/\ \   /\__  _\ /\  __ \      /\  ___\ /\ \   /\ "-.\ \   /\  __-.  ')
    print(r'\ \ \____  \ \ \/\ \  \ \ \____     \ \  __ \  \ \ \_\ \  \/_/\ \/ \ \ \/\ \     \ \  __\ \ \ \  \ \ \-.  \  \ \ \/\ \ ')
    print(r' \ \_____\  \ \_____\  \ \_____\     \ \_\ \_\  \ \_____\    \ \_\  \ \_____\     \ \_\    \ \_\  \ \_\\"\_\  \ \____- ')
    print(r'  \/_____/   \/_____/   \/_____/      \/_/\/_/   \/_____/     \/_/   \/_____/      \/_/     \/_/   \/_/ \/_/   \/____/ ')
    print(r'                                                                                                                       ')
    print(r' ______   __  __     ______        ______     __     ______     __  __     ______     ______    ')
    print(r'/\__  _\ /\ \_\ \   /\  ___\      /\  == \   /\ \   /\  ___\   /\ \_\ \   /\  ___\   /\  == \   ')
    print(r'\/_/\ \/ \ \  __ \  \ \  __\      \ \  __<   \ \ \  \ \ \____  \ \  __ \  \ \  __\   \ \  __<   ')
    print(r'   \ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ ')
    print(r'    \/_/   \/_/\/_/   \/_____/      \/_/ /_/   \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ ')
    print(r'                                                                                                ')
def YouHaveFindIt():
    print(r'__  __               __  __                    __________          __   _ __     __')
    print(r'\ \/ /___  __  __   / / / /___ __   _____     / ____/  _/___  ____/ /  (_) /_   / /')
    print(r' \  / __ \/ / / /  / /_/ / __ `/ | / / _ \   / /_   / // __ \/ __  /  / / __/  / / ')
    print(r' / / /_/ / /_/ /  / __  / /_/ /| |/ /  __/  / __/ _/ // / / / /_/ /  / / /_   /_/  ')
    print(r'/_/\____/\__,_/  /_/ /_/\__,_/ |___/\___/  /_/   /___/_/ /_/\__,_/  /_/\__/  (_)   ')
    print(r'                                                                                   ')
    print("\a")
    playsound('FindIt.mp3')
def FirstRun():
    # Connected by USB
    os.system("adb usb") 
    print("Connect To The Android Phone...")
    print("Please Make Sure The Interface is the Attack")
def check(SpoilsDic,MinGoldCoin=0,MinExlixir=0,MinDarkElixirDrill=0):
    if SpoilsDic["GoldCoin"] >= MinGoldCoin and SpoilsDic["Exlixir"] >= MinExlixir and SpoilsDic["DarkElixirDrill"] >= MinDarkElixirDrill:
        return True
    else:
        return False

# Drive Code
Welcome()
# FirstRun()
while True:
    os.system("adb exec-out screencap -p > screen.png")
    sleep(2)
    CropAndAnalyze.CropImage("screen.png",SpoilsLoc)
    Base64Str = CropAndAnalyze.LocalImageToBase64("Spoils.png")
    SpoilsDic = CropAndAnalyze.AnalyzeImage(AccessToken,Base64Str)
    if check(SpoilsDic,TarGoldCoin,TarExlixir,TarDarkElixirDrill):
        YouHaveFindIt()
        op = input("Do You Want Attack it?(y/n)")
        if op == 'y' or op == 'Y':
            break
        else:
            print("We will find the next one")
    os.system("adb shell input tap " + NextLoc[0] + ' ' + NextLoc[1])
    sleep(5)
