# -*- coding:utf-8 -*-
import turtle
import time


# 爱心的头部
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


# 这里输入要表白的内容，默认I Love you
love = input('输入表白内容，默认为"I Love you": ')
# 这里输入对方名字，没有则不执行
me = input('输入对方的姓名或者昵称: ')
if love == '':
    love = 'I Love you'

# 设置窗口的大小
turtle.setup(width=800, height=500)

# 设置颜色
turtle.color('red', 'pink')

# 设置笔粗细
turtle.pensize(5)

# 设置速度
turtle.speed(100)

# 设置提笔
turtle.up()

# 设置隐藏笔
turtle.hideturtle()

# 目标坐标,中心为0,0
turtle.goto(0, -180)
turtle.showturtle()

# 画出上线
turtle.down()
turtle.speed(1)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)

# 画爱心左边的顶部
LittleHeart()

# 画爱右边的顶部
turtle.left(120)
LittleHeart()

# 画出下线
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()

# 在爱心中写字 第一次
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('#CD5C5C', 'pink')

# 在爱心里写内容 font=可以设置字体 align=开始写字的位置
turtle.write(love, font=('gungsuh', 30,), align="center")
turtle.up()
turtle.hideturtle()
time.sleep(2)

# 在爱心里面写字 第二次
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('red', 'pink')
turtle.write(love, font=('gungsuh', 30,), align="center")
turtle.up()
turtle.hideturtle()

# 写对方名字
if me != '':
    turtle.color('black', 'pink')
    time.sleep(2)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(me, font=(20,), align="center", move=True)

# 关闭窗口
window = turtle.Screen()
window.exitonclick()
