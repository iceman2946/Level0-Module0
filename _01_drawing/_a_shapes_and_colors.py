import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Green = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Green.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Green.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Green.color('blue')
    Green.pencolor('orange')
    # Move your turtle forward using .forward(100)
    Green.forward(150)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    Green.right(90)
    # Now put the forward and left/right code into a for loop to repeat
    # 4 times.
    for i in range(4):
        Green.forward(150)
        Green.right(90)
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    Green.goto(-40,10)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    Green.circle(10)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    Green.begin_fill()
    for i in range(3):
        Green.forward(150)
        Green.right(120)
    # and .end_fill() below
    Green.end_fill()
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
