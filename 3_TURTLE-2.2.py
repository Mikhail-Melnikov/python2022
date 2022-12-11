from random import randint
import turtle


number_of_turtles = 7
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]

x = []
y = []
vx = []
vy = []
for i in range(len(pool)):
    pool[i].penup()
    x.append(randint(-200, 200))
    y.append(randint(-200, 200))
    pool[i].goto(x[i], y[i])
    pool[i].pendown()
    pool[i].speed(10)
    vx.append(randint(0, 20))
    vy.append(randint(0, 20))

size = 300

for i in range(steps_of_time_number):
    for j in range(len(pool)):
        x[j] += vx[j]
        y[j] += vy[j]
        if x[j] > size:
            x[j] = size*2 - x[j]
            vx[j] = - vx[j]
        if y[j] > size:
            y[j] = size*2 - y[j]
            vy[j] = -vy[j]
        if x[j] < -size:
            x[j] = -size + (-size - x[j])
            vx[j] = -vx[j]
        if y[j] < -size:
            y[j] = -size*2 - y[j]
            vy[j] = -vy[j]
        
        pool[j].goto(x[j], y[j])
