import turtle as tr

a = tr.Turtle()
win=tr.Screen()
win.bgcolor("grey10")
win.setup(1920,1080,0,0)
a.color("white")
a.ht()
a.width=20
a.speed(0)
color = ['white', "red", "blue", "green", "yellow", "skyblue", "magenta", "indigo", "wheat","orange","lime","brown","pink"]
x = 1
y = 45
j = 0
while True:
    if j == 13:
        j = 0
    for i in range(4):
        a.fd(x)
        a.left(90)
    a.color(color[j])
    x += 2
    y += 1
    j += 1
    a.setheading(y + 45)
