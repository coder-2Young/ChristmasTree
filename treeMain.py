from tree import *

# 背景改为黑色
screensize(bg='black')
setup(500, 700, startx=None, starty=None)
title("Merry Christmas")
speed(0)
pencolor("green")
pensize(10)
hideturtle()
changeMypos(0, 185, 0)

# 树顶层
seth(-120)
Rightdraw(10, 12, 2)
changeMypos(0, 185, -60)
Leftdraw(10, 12, 2)
changeMypos(xcor(), ycor(), -150, 10)
# 第一层的波浪
for i in range(4):
    Rightdraw(5, 7, 15)
    seth(-150)
    penup()
    fd(2)
    pendown()
# 二层
changeMypos(-55, 70, -120)
Rightdraw(10, 8, 5)
changeMypos(50, 73, -60)
Leftdraw(10, 8, 5)
changeMypos(xcor(), ycor(), -120, 10)
seth(-145)
pendown()
# 第二层的波浪
for i in range(5):
    Rightdraw(5, 9, 15)
    seth(-152.5)
    penup()
    fd(3)
    pendown()
# 树三层
changeMypos(-100, 0, -120)
Rightdraw(10, 6.5, 4.5)
changeMypos(80, 0, -50)
Leftdraw(10, 6, 3)
changeMypos(xcor(), ycor(), -120, 10)
seth(-145)
# 第三次的波浪
for i in range(6):
    Rightdraw(5, 9, 15)
    seth(-152)
    penup()
    fd(3)
    pendown()
# 树四层
changeMypos(-120, -55, -130)
Rightdraw(7, 10, 4)
changeMypos(100, -55, -50)
Leftdraw(7, 10, 5)
changeMypos(xcor(), ycor(), -120, 10)
seth(-155)
# 第四层的波浪
for i in range(7):
    Rightdraw(5, 9, 13)
    seth(-155)
    penup()
    fd(3)
    pendown()
# 树根
changeMypos(-70, -120, -95)
Leftdraw(3, 8, 3)
changeMypos(70, -120, -95)
Rightdraw(3, 8, 3)
changeMypos(xcor(), ycor(), -170, 10)
Rightdraw(10, 12, 2)
# 画树枝
drawBranch(45, -80)
drawBranch(-70, -25)
drawBranch(-20, 40)

# 添加挂件
drawHat(-25, 175, -10, 2.5)
drawCandy(-75, -50, -10, 1)
drawCandy(10, 40, -10, 1.2)
drawStar(110, -90, 80, 1)
drawStar(-120, -100, 50, 0.8)
drawStar(-90, -50, 20, 0.9)
drawStar(90, -25, 30, 1.1)
drawSock(10, -35, -10, 2)
drawSock(-40, 100, 10, 1)
drawStar(-20, 40, 30, 1)
drawStar(10, 120, 90, 1)

# 打印祝福语
color("dark red", "red")  # 定义字体颜色
penup()
goto(0, -230)
write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小

# 打印祝福语
color("white")  # 定义字体颜色
penup()
goto(0, -270)
write("Every day with you is happy", align="center", font=("Comic Sans MS", 20, "bold"))  # 定义文字、位置、字体、大小

# 调用下雪的函数
drawSnow()

done()