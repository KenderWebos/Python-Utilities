import pyautogui as pagui

#pagui.displayMousePosition()

x=1360
y=766

num1 = 15
num2 = 404

pagui.click(num1, num2)

if pagui.pixel(num1, num2)[0] == 30:
    print("funcionando")