import pyautogui
from time import sleep

#encontrar a posicao de algo
#fazer algo com essa posicao
""" pyautogui.moveTo(976,339, duration=2)
for i in range(500): 
    sleep(0.2)
    pyautogui.click()    """

pyautogui.click(x=569,y=753, duration=1.5)
pyautogui.click(x=673,y=231, duration=1.5)
pyautogui.rightClick()
pyautogui.move(5, 250, duration=1.5)
pyautogui.click()
pyautogui.move(300, 0,duration=2)
pyautogui.click()
 