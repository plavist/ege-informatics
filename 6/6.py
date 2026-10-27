from turtle import *
tracer(0)
step = 15

left(90)
for _ in range(6):
    forward(24*step)
    right(90)
    forward(30*step)
    right(90)
up()

forward(2*step)
right(90)
forward(10*step)
left(90)

down()

for _ in range(6):
    forward(75*step)
    right(90)
    forward(71*step)
    right(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*step, y*step)
        dot(3, 'red')

update()
done()