import pyautogui


pyautogui.PAUSE = 0.3

#.click - clica
#.write - texto
#.press - aperta uma tecla
#.hotkey - aperta atalho

pyautogui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('comet')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
