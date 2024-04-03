import pyautogui as py
import time
py.PAUSE = 2
py.press('win')
py.write('bloco de notas')
py.press('enter')
#time.sleep(10)
py.hotkey('ctrl','s')
py.write('nada.bat')
py.press('enter')
py.write("@echo on color 02 :loop echo nada goto :loop")
py.hotkey("ctrl" , "s")