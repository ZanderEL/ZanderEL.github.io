'''
Alexander Lambach
An abstract scene using one of each starter functions with varius sizes and colors
'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

# Define the setup function to set up the background of the scene
def setup(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

# Define the jump_circle function to make a circle and jump to the next position
def jump_circle(t):
    draw_circle(t,25,"green")
    jump_to(t,100,100)

# Define the jump_curve function to make a curve and jump to the next position
def jump_curve(t):
    draw_curve(t, 200, 50, 10,)
    jump_to(t,100,-100)

# Define the jump_polygon function to make a polygon and jump to the next position
def jump_polygon(t):
    draw_polygon(t, 8, 75, "red")
    jump_to(t, -100, -100)

# Define the jump_rectangle function to make a rectangle and jump to the next position
def jump_rectangle(t):
    draw_rectangle(t, 50, 100)
    jump_to(t, -200, 100)


def jump_sqaure(t):
    draw_square(t, 100, "purple")
    jump_to(t, 0, 200)

#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Defined functions to create shapes and setup the background and automatically jump to the next position"""
    
    # Called all of the following functions to make the same scene
    setup(t)
    jump_circle(t)
    jump_curve(t)
    jump_polygon(t)
    jump_rectangle(t)
    jump_sqaure(t)
    draw_triangle(t, 50, "sandy brown")
    

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()