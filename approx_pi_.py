#--------------------------------------------------------------------#
#
#  APPROXIMATE PI
#
#  Finds an approximation to the irrational number pi, based on 
#  the likelihood of a randomly-tossed pin, landing at a particular
#  angle, intersecting a fixed line.
#
#--------------------------------------------------------------------#

from turtle import *
from random import randint

reset() # Create an empty window (you can delete this line if you wish)

#Setting up Variables/Constants for use.
#You can change these for different effects:
number_of_lines = 4
number_of_pins = 150
screen_size = 800

#Some expressions and variables for our program to run (don't edit these):
line_placement = screen_size/number_of_lines
pin_length = line_placement/2
maxcoords = screen_size/2
line_crosses = 0
line_positions = []

#Setting up the screen size, colour, drawing speed, etc.
setup(screen_size, screen_size)
bgcolor("yellow")
speed("fastest")
penup()
hideturtle()
width(4)
pencolor("black")
title("Approximation of Pi: Pending... using %s pins and %s lines" %(number_of_pins, number_of_lines))



#Creation of the black lines and saving their x coordinates for future use.
def black_line_creation():
    goto(-maxcoords-pin_length, maxcoords)
    for linecount in range(number_of_lines):
        goto(xcor()+line_placement,ycor()) #Go to the next line position
        pendown()
        goto(xcor(),-maxcoords) 
        penup()
        goto(xcor(),maxcoords)
        line_positions.append(xcor()) #Save the position of lines.


#Creation of pin dropping function and detection of line crosses.
def drop_pins():
    global line_crosses
    for pin_count in range(number_of_pins):
        #Generate pin placement and go there.
        xcoord_pin_start = randint(-maxcoords, maxcoords) 
        ycoord_pin_start = randint(-maxcoords, maxcoords)
        goto(xcoord_pin_start, ycoord_pin_start)

        #Generate a heading (0-359 degrees) and remember where the other end of the pin is.
        random_heading = (randint(0,359))
        setheading(random_heading)
        forward(pin_length)
        xcoord_pin_end = xcor()

        #Draw a red pin if it crosses a line else draw a blue one after checking all possible lines.
        for line_number in line_positions:
            if  (line_number > xcoord_pin_start and line_number < xcoord_pin_end) or \
                (line_number < xcoord_pin_start and line_number > xcoord_pin_end) or \
                (line_number == xcoord_pin_start and line_number == xcoord_pin_end):
                pencolor("red")
                line_crosses = line_crosses +1 #We crossed a line, add a tally to the count.
                draw_pin(xcoord_pin_start, ycoord_pin_start, random_heading)
                break
            elif line_number == line_positions[-1]:
                pencolor("blue")
                draw_pin(xcoord_pin_start, ycoord_pin_start, random_heading)
                break    

#Function to actually draw the pins, used by the 'drop_pins' function.
def draw_pin(xcoord_pin_start, ycoord_pin_start, random_heading):
        goto(xcoord_pin_start, ycoord_pin_start)
        pendown()
        dot(10)
        setheading(random_heading)
        forward(pin_length)
        penup()


#Function to calculate the approximation of pi, and display on screen and in title.
def pi_approximation_calc(line_crosses):
    goto(0,0)
    color("dark green")
    if line_crosses == 0:
        title("No lines were crossed! Could not approximate Pi!")
        write("No lines were crossed! Could not approximate Pi!", \
        True, align="center", font=("Arial", 12, "bold"))
    else:
        approximation = (float(number_of_pins)/line_crosses)
        title("Approximation of Pi: %s using %s pins and %s lines" \
        %(approximation, number_of_pins, number_of_lines))
        write("Approximation of Pi: %s using %s pins and %s lines" \
        %(approximation, number_of_pins, number_of_lines), True, align="center", font=("Arial", 12, "bold"))


#Calling our line creation and pin droppping functions
black_line_creation()
drop_pins()
pi_approximation_calc(line_crosses)


#Finished! Release the drawing window.
done()

#--------------------------------------------------------------------#
