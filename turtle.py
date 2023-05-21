import turtle 
colors=["violet","red","blue","green","yellow","pink"]
turtle.tracer(0,0)
for i in range(45):
    turtle.color(colors[i%6])
    turtle.pendown()
    turtle.forward(2+i*5)
    turtle.left(45)
    turtle.width(i)
    turtle.penup()
    turtle.update()
