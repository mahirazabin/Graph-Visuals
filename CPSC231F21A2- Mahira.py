# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
#NAME: MAHIRA ZABIN
# Tutorial: T07
# ID: 30150211
# Date: 22ND OCT, 2021
# Description: CREATE A PROGRAM THAT DRAWS EQUATIONS AND MARKS THE MAXIMUM AND MINIMUM POINTS
#REFERENCE: https://thispointer.com/python-how-to-use-global-variables-in-a-function/#:~:text=with%20same%20name%20%3F-,Use%20of%20%E2%80%9Cglobal%E2%80%A0keyword%20to%20modify%20global%20variable%20inside,at%20start%20of%20function%20i.e.

from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
GLOBALMINX = 100000
GLOBALMINY = 100000
GLOBALMAXX = -100000
GLOBALMAXY = -100000
AXIS_COLOR = "black"


def get_color(equation_counter):
    if equation_counter % 3 == 0:
        return "red"
    elif equation_counter % 3 == 1:
        return "green"
    elif equation_counter % 3 == 2:
        return "blue"


    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    # DEFAULT return black, needs to be changed




def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """

    screenX= x_origin + x * ratio
    screenY= y_origin + y * ratio

    return screenX, screenY


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """

    calc_minX = int(-x_origin / ratio)
    calc_maxX = int((WIDTH - x_origin) / ratio)

    return calc_minX, calc_maxX




def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """

    calc_minY = int(-y_origin / ratio)
    calc_maxY = int((HEIGHT - y_origin) / ratio)

    return calc_minY, calc_maxY


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x1, screen_y1)
    pointer.pendown()
    pointer.goto(screen_x2,screen_y2)



def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x,screen_y)
    pointer.pendown()
    pointer.goto(screen_x, screen_y + 10)
    pointer.goto(screen_x, screen_y - 10)




def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x,screen_y)
    pointer.goto(screen_x, screen_y - 20)
    pointer.write(label_text)


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x,screen_y)
    pointer.pendown()
    pointer.goto(screen_x + 10, screen_y)
    pointer.goto(screen_x -10, screen_y)


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x,screen_y)
    pointer.goto(screen_x - 20, screen_y)
    pointer.write(label_text)



def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    pointer.penup()
    minValue, maxValue = calc_minmax_x(x_origin, ratio)
    pointer.goto(0,y_origin)
    pointer.pendown()
    pointer.goto(WIDTH, y_origin)
    #


    for i in range(minValue, maxValue+1):
        x_screen,y_screen = calc_to_screen_coord(i,0,x_origin,y_origin,ratio)
        draw_x_axis_tick(pointer, x_screen, y_screen)
        draw_x_axis_label(pointer, x_screen, y_screen, str(i))



def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pointer.penup()
    minValue, maxValue = calc_minmax_y(y_origin, ratio)
    pointer.goto(x_origin,0)
    pointer.pendown()
    pointer.goto(x_origin, HEIGHT)
    #


    for i in range(minValue, maxValue+1):
        x_screen,y_screen = calc_to_screen_coord(0,i,x_origin,y_origin,ratio)
        draw_y_axis_tick(pointer, x_screen, y_screen)
        draw_y_axis_label(pointer, x_screen, y_screen, str(i))


def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    global GLOBALMINX,GLOBALMINY ,GLOBALMAXX ,GLOBALMAXY
    left, right= calc_minmax_x(x_origin,ratio)

    pointer.penup()
    y = calc(expr, left)
    ScreenX, ScreenY= calc_to_screen_coord(left,y,x_origin,y_origin,ratio)
    pointer.goto(ScreenX, ScreenY)

    i = left
    forwardX = left + 0.1
    forwardY= calc(expr, forwardX)
    globalMinimumX = 100000
    globalMinimumY = 100000
    globalMaximumX = -100000
    globalMaximumY = -100000


    if forwardY > y:
        goingUp = True

    else:
        goingUp = False

    radius= 10

    while (i <= right):
        i= i + 0.1
        y= calc(expr, i)


        ScreenX, ScreenY = calc_to_screen_coord(i, y, x_origin, y_origin, ratio)
        pointer.color(colour)
        pointer.pendown()
        pointer.goto(ScreenX,ScreenY)
        forwardX = i + 0.1
        forwardY = calc(expr, forwardX)




        if forwardY > y and goingUp == False:
            pointer.penup()
            pointer.goto(ScreenX, ScreenY - 10)
            pointer.pendown()
            pointer.color("orange")
            pointer.circle(radius)
            pointer.penup()
            goingUp = True
            pointer.goto(ScreenX,ScreenY)
            if y < globalMinimumY :
                globalMinimumX = i
                globalMinimumY = y
            if y < GLOBALMINY :
                GLOBALMINY = y
                GLOBALMINX = i


        elif forwardY < y and goingUp == True:
            pointer.penup()
            pointer.goto(ScreenX, ScreenY - 10)
            pointer.pendown()
            pointer.color("purple")
            pointer.circle(radius)
            pointer.penup()
            goingUp = False
            pointer.goto(ScreenX,ScreenY)
            if y > globalMaximumY :
                globalMaximumX = i
                globalMaximumY = y
            if y > GLOBALMAXY :
                GLOBALMAXX = i
                GLOBALMAXY = y


    if (globalMaximumX == -100000):
        print("No expression global maximum")

    else:
        print("Expression global maximum (", globalMaximumX,",", globalMaximumY, ")" )

    if (globalMinimumX == 100000):
        print("No expression global minimum")
    else:
        print("Expression global minimum (", globalMinimumX, ",", globalMinimumY, ")")









# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """


    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1

    print("Global maximum for all expressions (", GLOBALMAXX, ",", GLOBALMAXY, ")")
    print("Global minimum for all expressions (", GLOBALMINX,",", GLOBALMINY , ")" )



main()
turtle.exitonclick()

