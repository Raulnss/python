import pyautogui as py
import time
py.PAUSE = 2
py.press('win')
py.write('visual studio code')
py.press('enter')
#time.sleep(10)
py.hotkey('ctrl','n')
py.hotkey('ctrl','s')
py.write('teste.html')
py.press('enter')
py.write('html:5')
time.sleep(5)
py.press('enter')