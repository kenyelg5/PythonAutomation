import pyautogui

pyautogui.PAUSE = 0.5



pyautogui.press('win')
pyautogui.write('comet')
pyautogui.press('enter')
link = 'https://github.com/kenyelg5'
pyautogui.typewrite(link)
pyautogui.press('enter')
