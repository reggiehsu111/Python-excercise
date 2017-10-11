import turtle

def draw_square(some_turtle,forward1,forward2):
    some_turtle.begin_fill()
    for x in range(2):
        some_turtle.forward(forward1)
        some_turtle.right(90)
        some_turtle.forward(forward2)
        some_turtle.right(90)
    some_turtle.end_fill()

def change_pos(some_turtle,angle,length):
    some_turtle.color("white")
    some_turtle.right(angle)
    some_turtle.forward(length)
    some_turtle.color("red")


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)

    brad.right(45)
    draw_square(brad,50,25)
    change_pos(brad,135,75)
    brad.left(180)
    draw_square(brad,100,25)

    var = 0
    while var<360/5:
        draw_square(brad)
        brad.right(5)
        var=var+1


    angie = turtle.Turtle()
    angie.circle(100)
    angie.shape("arrow")
    angie.color("blue")

    window.exitonclick()

draw_art()