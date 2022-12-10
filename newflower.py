import turtle as t
import colorsys 

t.speed(0)
t.bgcolor('black')
t.pensize(2)

for i in range(16):
    t.begin_fill()

    for j in range(10):
        c=colorsys.hsv_to_rgb(i/15,j/20,1)
        t.color(c)
        t.rt(90)
        t.circle(150-j*6,90)
        t.lt(90)
        t.circle(150-j*6,90)
        t.rt(180)

    t.circle(40,24)
    t.end_fill()
t.done()