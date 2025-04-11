import turtle
turtle.screensize(800,600,'pink')
turtle.width(10)

turtle.color('blue')
turtle.circle(50)
turtle.penup()
turtle.goto(120,0)
turtle.pendown()

turtle.color('black')
turtle.circle(50)
turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color('red')
turtle.circle(50)
turtle.penup()
turtle.goto(60,-40)
turtle.pendown()

turtle.color('yellow')
turtle.circle(50)
turtle.penup()
turtle.goto(180,-40)
turtle.pendown()
turtle.color('green')
turtle.circle(50)




import turtle
t=turtle.Pen()
c=('blue','black','red','yellow','green')
t.width(4)
t.speed(100)
for i in range(50):
    #t.color(c)错误展示
    t.goto(0,-10*i)
    t.pendown()
    t.color(c[i%len(c)])
    t.circle(10*i+10)
    t.penup()
turtle.done()