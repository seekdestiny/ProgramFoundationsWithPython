import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
     window = turtle.Screen()
     window.bgcolor("red")
     brad = turtle.Turtle()
     brad.shape("turtle")
     brad.color("yellow")
     brad.speed(2)
    
     for i in range(1,36):
         draw_square(brad)
         brad.right(10)
     #angie = turtle.Turtle()
     #angie.shape("arrow")
     #angie.color("blue")
     #angie.circle(100)

     #andy = turtle.Turtle()
     #andy.shape("arrow")
     #angie.color("green")
     #angie.speed(2)
     #for index in range(3):
     #    angie.left(120)
     #    angie.forward(100)

     window.exitonclick()

draw_art()
