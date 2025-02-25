import turtle
import easygui
import random

__Pen = turtle.Pen()

c = turtle.numinput('严智琦', '请输入抽到的人数')
for i in range(int(c)):
    a=random.randint(1, 62)
    if a == 44:
        a += 1
    if a == 2:
        a += 1
    easygui.msgbox(a)

