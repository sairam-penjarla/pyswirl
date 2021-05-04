import turtle
colors = ['#537c78', '#7ba591', '#cc222b', '#f15b4c', '#faa41b', '#ffd45b']
angle = int(input("enter the angle: \n"))
dist = 1
flag = 5000
spiral = turtle.Turtle()
spiral.speed(100)
for dist in range(flag):
    spiral.forward(dist)


    #uncomment the following lines to add color and change with to your lines


    #spiral.pencolor(colors[dist % 6])
    #spiral.width(dist / 100 + 1)




    # To create circular pattenrs, uncomment the below line and comment out the above line
    # OR DONT :D
    #spiral.circle(dist)






    spiral.right(angle)





    #uncomment and experiment with the folowwing lines and find more unique patterns
    """spiral.forward(dist)
    spiral.right(60)
    spiral.forward(dist)
    spiral.right(60)
    spiral.forward(dist)
    spiral.right(60)"""
turtle.done()
