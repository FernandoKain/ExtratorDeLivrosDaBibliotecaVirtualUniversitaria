import pyautogui
import time


# print(pyautogui.position())
pyautogui.sleep(2)


def recorte():
    pyautogui.hotkey('winleft', 'shift', 's')
    time.sleep(1)
    pyautogui.mouseDown(x=650, y=99)
    pyautogui.moveTo(x=1255, y=978)
    pyautogui.mouseUp()


def alttab1():
    pyautogui.keyDown('alt')
    #time.sleep(.1)
    pyautogui.press('tab')
    #time.sleep(.1)
    pyautogui.keyUp('alt')


def alttab2():
    pyautogui.keyDown('alt')
    #time.sleep(.1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    #time.sleep(.1)
    pyautogui.keyUp('alt')


def virarpaginadireita():
    pyautogui.click(x=1840, y=572)
    time.sleep(4)


def zoomout():
    pyautogui.moveTo(x=960, y=440)
    pyautogui.keyDown('ctrl')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')

def zoomin():
    pyautogui.moveTo(x=960, y=440)
    pyautogui.keyDown('ctrl')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.press('+')
    pyautogui.keyUp('ctrl')


def presentf11():
    pyautogui.press('f11')


def colar():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')


def ajustedacolagem():
    time.sleep(1)
    pyautogui.rightClick(x=960, y=440)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('2')
    pyautogui.press('8')
    pyautogui.press(',')
    pyautogui.press('8')
    pyautogui.press('5')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('1')
    pyautogui.press('9')
    pyautogui.press(',')
    pyautogui.press('8')
    pyautogui.press('7')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('right')



# print(pyautogui.position())



# Primeiro acesso, entrando em modo apresentação
alttab1()
presentf11()


for i in range (1):
    zoomout()
    recorte()
    zoomin()
    alttab2()
    colar()
    ajustedacolagem()
    alttab1()
    virarpaginadireita()

for i in range (7):
    zoomout()
    recorte()
    zoomin()
    alttab1()
    colar()
    ajustedacolagem()
    alttab1()
    virarpaginadireita()
