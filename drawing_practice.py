import turtle

def main():
    screen = turtle.Screen()
    screen.colormode(200)
    drawing = turtle.Turtle()
    drawing.speed("fast")
    drawing.color("green")

    for i in range(1000):
        drawing.left(200)
        drawing.forward(300 + i)



    turtle.exitonclick()

if __name__ == "__main__":
    main()