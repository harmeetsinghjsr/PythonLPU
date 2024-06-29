import pyautogui, time

time.sleep(5)

f = open("C:/Users/hs978/CodeSpace/Python Programs/Autotype/answer.txt", 'r')

for line in f:
    pyautogui.typewrite(line.strip())
    pyautogui.press("enter")