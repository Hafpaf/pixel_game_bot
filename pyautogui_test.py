import pyautogui

print("Mousepos:", pyautogui.position())
print("Screen", pyautogui.size())
box_x = (296, 82)
box_y = (1044, 709)
print("Within the box: ", pyautogui.onScreen(296, 82))
exit()
