import turtle
from turtle import Turtle, colormode
import random
import colorgram

def rand_turt_color():
    timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def turtle_shapes():
    print(timmy)
    timmy.penup()
    timmy.setpos(-50, 200)
    timmy.pendown()
    timmy.width(3)
    for shapes in range(3, 17):
        rand_turt_color()
        angle = 360 / shapes
        for sides in range(shapes):
            timmy.forward(100)
            timmy.right(angle)

def lost_turtle():
    print(timmy)
    timmy.width(5)
    timmy.speed('fast')
    paces = 0
    while paces < 7200:
        rand_turt_color()
        timmy.setheading(random.randint(1,4)*90)
        timmy.forward(20)
        paces += 1

def spirograph(circles):
    print(timmy)
    timmy.speed('fastest')
    angle = 0
    while angle < 360:
        rand_turt_color()
        timmy.circle(150)
        timmy.right(360/circles)
        angle += 360/circles


def artist_turtle():
    #get colors
    artist_colors = []
    dot_colors = colorgram.extract('galaxy-space-chromebook-wallpaper.jpg', 100)
    for colors in dot_colors:
        r = colors.rgb.r
        g = colors.rgb.g
        b = colors.rgb.b
        new_color = (r,g,b)
        artist_colors.append(new_color)
    random.shuffle(artist_colors)
    #move turtle to start
    timmy.penup()
    my_screen = turtle.Screen()
    timmy.goto(-200, 200)
    column = 0
    color_pick = 0
    turtle_y = timmy.ycor()
    #draw
    while color_pick < 100:
        while column < 10:
            timmy.pendown()
            timmy.dot(20, random.choice(artist_colors))
            timmy.penup()
            timmy.forward(50)
            color_pick += 1
            column += 1
        turtle_y = timmy.ycor() - 50
        timmy.goto(-200, turtle_y)
        column = 0



    my_screen.exitonclick()


print("What would you like the turtle to do? Type '1' for loading screen,")
choice = input("'2' for random walk, or '3' for spirograph, or '4' for modern art: ")

timmy = Turtle()
colormode(255)
timmy.shape("turtle")

if choice == "1":
    turtle_shapes()
    my_screen = turtle.Screen()
    my_screen.exitonclick()
elif choice == "2":
    lost_turtle()
    my_screen = turtle.Screen()
    my_screen.exitonclick()
elif choice == "3":
    print("How dense would you like the spirograph?")
    density = int(input("(8 for sparse, 120+ for dense): "))
    spirograph(density)
    my_screen = turtle.Screen()
    my_screen.exitonclick()
else:
    artist_turtle()






