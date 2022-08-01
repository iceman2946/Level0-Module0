import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    Grizzly.penup()
    # 7. Move the turtle to a new location using .goto(x, y)
    Grizzly.goto(x,y)

def turtle_clicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
    for i in range(3):
        Grizzly.right(360)
        # 9. Make the turtle spin 360 degrees using the .right() method
        
        # 10. Use the .color() method and getRandomColor() function to change
        # the color of the turtle,
        Grizzly.color(get_random_color())


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    Grizzly=turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    Grizzly.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    Grizzly.color('green')
    Grizzly.pencolor('red')
    # 4. Set and new width, length, and outline of our turtle
    Grizzly.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

    # 5. Uncomment the following line and replace 'my_turtle' with your turtle
    Grizzly.onclick(turtle_clicked)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done()
