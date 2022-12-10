import turtle as t
t.bgcolor('black')
t.speed(100)
t.hideturtle()

color =['blue','purple','blue','purple']

for i in range(120):
    for c in color:
        t.color(c)
        t.circle(200-i,100)
        t.lt(90)
        t.circle(200-i,100)
        t.end_fill()
t.mainloop()