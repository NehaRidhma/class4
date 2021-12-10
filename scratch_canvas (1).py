import turtle

length = int(input('enter length value'))
breadth = int(input('enter breadth value'))
for r in range(0, 2):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(breadth)
    turtle.left(90)
