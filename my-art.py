from turtle import *
from colorsys import *

# Setup
setup(880, 725)
speed(0) # '0' is the fastest speed for turtle
tracer(10)
bgcolor("black")

h = 0
# Create the loop
for i in range(360):
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    circle(150)
    left(5) # Adding a turn makes the pattern bloom

done()