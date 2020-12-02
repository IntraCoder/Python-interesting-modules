import turtle
a = turtle.Turtle()
a.shape("turtle")
a.screen.bgcolor("black") #specify window background color
a.color("white")
a.speed(0)
a.ht()
c=['green','red','white','pink','purple','blue','grey']
d=['yellow','orange','red','lightgreen']
a.right(45)
def triangle(col_list,x,y):
    j=0
    for i in range(y):
        a.color(c[j])
        a.circle(x,None)
        x+=1
        j+=1
        if j>(len(col_list)-1):
            j=0
def splash():
    a.home()

for i in range(2):
    triangle(c,2,60)
    a.left(180)



turtle.mainloop()
