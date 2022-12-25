from turtle import *
from random import *
import math


# 绘图方法
def Rightdraw(Range, Fd, Right):
    for i in range(Range):  # Range循环次数
        fd(Fd)  # 向前Fd个距离
        right(Right)  # 在当前行进方向再向右偏转Right度


def Leftdraw(Range, Fd, Left):
    for i in range(Range):  # Range循环次数
        fd(Fd)  # 向前Fd个距离
        left(Left)  # 在当前行进方向再向右偏转Right度


# 重设海龟位置
def changeMypos(x, y, range=heading(), Fd=0):
    penup()
    goto(x, y)
    seth(range)
    fd(Fd)
    pendown()


def drawBranch(x, y, size=1):
    changeMypos(x, y)
    Leftdraw(6, 3, 9)
    seth(0)
    Rightdraw(6, 3, 9)
    seth(0)
    fd(6)


# 画五角星
def drawStar(x, y, Range, size):
    pensize(2)
    color("yellow")
    begin_fill()
    changeMypos(x, y, Range)
    for i in range(5):  # 画五角星
        forward(10 * size)
        right(144)  # 五角星的角度
        forward(10 * size)
        left(72)  # 继续换角度
    end_fill()
    right(126)


# 绘制雪花
def drawSnow():
    hideturtle()
    speed(0)
    for i in range(50):  # 雪花数量
        penColor = choice(["#F0FFFF", "#F8F8FF", "#FFFFF0","#F0F8FF","#B0C4DE"]) # 随机选色号，白色蓝色类
        pencolor(penColor)
        pensize(2)
        changeMypos(randint(-248, 248), randint(-100, 248))
        petalNumber = choice([6,8])  # 雪花花瓣数为6或8
        snowSize = int(randint(2, 8))
        for j in range(petalNumber):
            fd(snowSize)
            backward(snowSize)
            right(360 / petalNumber)


# 圣诞袜子
def drawSock(x, y, range, size=1):
    # 绘制袜子的白边
    pensize(2)
    changeMypos(x, y, range)
    color("black", "white")
    begin_fill()
    fd(20 * size)
    circle(3 * size, 180)
    fd(20 * size)
    circle(3 * size, 180)
    end_fill()
    # 绘制袜子的下半部分
    color("white", "red")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 18 * size * (math.cos(math.radians(range)))
    finaly = y + 18 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range - 90)
    fd(20 * size)  # 圆弧距离白边40
    seth(180 + range)
    fd(5 * size)  # 向袜子头延伸10
    circle(7 * size, 180)  # 袜子头处的半圆形
    fd(17 * size)  # 袜子宽42
    circle(4 * size, 90)
    #seth(90 + range)
    d = distance(finalx, finaly)  # 找到袜子底部与白边的距离
    fd(d)
    seth(range + 180)
    fd(16 * size)
    end_fill()


# 圣诞帽
def drawHat(x, y, range, size=1):
    # 绘制帽白边
    pensize(2)
    changeMypos(x, y, range)
    color("white", "white")
    begin_fill()
    fd(20 * size)
    circle(-3 * size, 180)
    fd(20 * size)
    circle(-3 * size, 180)
    end_fill()
    # 绘制帽子上半部分
    color("white", "red")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 18 * size * (math.cos(math.radians(range)))
    finaly = y + 18 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range + 90)
    Rightdraw(18, 2 * size, 7)
    seth(190)
    Leftdraw(9, 2 * size, 8)
    goto(finalx, finaly)
    goto(startx, starty)
    end_fill()
    # 绘制圣诞帽上的小球
    changeMypos(startx, starty, range + 90)
    Rightdraw(18, 2 * size, 7)
    begin_fill()
    color("white", "white")
    circle(-2.5 * size)
    end_fill()


# 绘制彩带
def drawRibbon(x, y, range, size):
    begin_fill()
    color("red", "red")
    seth(range + 40)
    fd(15 * size * math.tan(math.radians(range + 40)))
    seth(range + 90)
    fd(20 / 3 * size)
    seth(range - 140)
    fd(15 * size * math.tan(math.radians(range + 40)))
    seth(range - 90)
    fd(20 / 3 * size)
    end_fill()


# 圣诞糖果
def drawCandy(x, y, range, size):
    # 绘制糖体
    pensize(1)
    changeMypos(x, y, range)
    color("white", "white")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 8 * size * (math.cos(math.radians(range)))
    finaly = y + 8 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range + 90, 40 * size)
    circle(-40 / 3 * size, 180)
    circle(-8 / 3 * size, 180)
    circle(22 / 3 * size, 180)
    goto(finalx, finaly)
    goto(startx, starty)
    end_fill()
    # 绘制下面三条彩带
    color("white")
    changeMypos(startx, starty, range + 90)
    fd(10 / 3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    changeMypos(xcor(), ycor(), range + 90, 13.3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    changeMypos(xcor(), ycor(), range + 90, 13.3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    # 绘制弧线段的彩带
    changeMypos(startx, starty, range + 90, 40 * size)
    circle(-13.3 * size, 55)
    x1 = xcor()
    y1 = ycor()
    begin_fill()
    circle(-13.3 * size, 80)
    right(75)
    fd(6.3 * size)
    right(115)
    circle(7 * size, 85)
    goto(x1, y1)
    end_fill()


