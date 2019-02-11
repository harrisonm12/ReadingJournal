import turtle

#------------------------------------------------------------------------------
# Starter code to get things going
# (feel free to delete once you've written your own functions
#------------------------------------------------------------------------------

# Create the world, and a turtle to put in it
bob = turtle.Turtle()
#------------------------------------------------------------------------------
# Make some shapes
#   Work through exercises 1-4 in Chapter 4.3.
#------------------------------------------------------------------------------

# NOTE: for part 2 of 4.3, you will add another parameter to this function
def square(t,length):
    """
    Draw a square using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don)
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

## Polygon
def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

## Circle
def circle(t,r):
    circumference = 2 * 3.14159 * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

#Exercise 5
def draw_archimedian_spiral(t, n, length, a, b):
    #I received a decent amount of help from the wikipedia page provided in the book and from Downey's code to help me learn what theta was and what parameters were neccesary in the function
    #a determines how loose the spiral begins as.  A larger a means a looser draw_archimedian_spiral
    #b determines how tightly coiled the spiral overall is.  A larger b means looser spirals
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


circle(bob,50)
bob.pu()
bob.fd(100)
bob.pd()
polygon(bob,6,50)
bob.pu()
bob.rt(90)
bob.fd(100)
bob.pd()
square(bob,50)

# Wait for the user to close the window
turtle.mainloop()
#------------------------------------------------------------------------------
# Make some art
#   Complete *at least one of* Exercise 2, 3, 4, or 5 in `shapes.py`.
#------------------------------------------------------------------------------

# If you come up with some cool drawings you'd like to share with the rest of the class, let us know!
