https://trinket.io/python/88dd6c94d1

from PIL import Image
im = Image.open("/home/jack/Desktop/R-Studio/qt-colors.png") 
im

# http://interactivepython.org/runestone/static/thinkcspy/index.html

import turtle
from myturtle import MyTurtle, create_turtles, move_turtles, writer

number_of_turtles = 10

screen = turtle.Screen()

def draw_shape(x, y, n = 20, clear = True):
  if clear:
    writer.clear()
  screen.tracer(0)
  for turtle in screen.turtles():
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
  screen.tracer(1)
  for i in range(n):
    screen.tracer(0)
    move_turtles(screen)
    screen.tracer(1)

create_turtles(screen, number_of_turtles)

draw_shape(0,-150, clear = False)

screen.onclick(draw_shape)

screen.listen()
turtle.done()

turtle.done()
turtle.reset()
turtle.clear()

turtle.clear()

!python myturtle.py

# Inspired by Brad Miller's illustration for How to Think like a
# Computer Scientist:
# http://interactivepython.org/runestone/static/thinkcspy/index.html

import turtle
from myturtle import MyTurtle, create_turtles, move_turtles, writer

number_of_turtles = 10

screen = turtle.Screen()

def draw_shape(x, y, n = 20, clear = True):
    if clear:
        writer.clear()
        screen.tracer(0)
    for turtle in screen.turtles():
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        screen.tracer(1)
    for i in range(n):
        screen.tracer(0)
        move_turtles(screen)
        screen.tracer(1)

create_turtles(screen, number_of_turtles)
draw_shape(0,-150, clear = False)
screen.onclick(draw_shape)
screen.listen()
turtle.done()

import turtle
import time


def draw_rect(t):
    for i in range(0, 4):
        t.forward(100)
        t.right(90)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_circle(t):
    for i in range(0, 200):
        t.circle(50+i)  
        t.left(120+i)
        t.forward(100+i)    

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_triangle(t):
    t.forward(100)

    for i in range(0, 200):
        t.left(120+i)
        t.forward(100+i)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


draw_triangle(turtle)

draw_circle(turtle)

%%writefile myturtle.py
import turtle
from time import sleep
class MyTurtle(turtle.Turtle):
    def __init__(self, screen = turtle.Screen()):
        turtle.Turtle.__init__(self, screen)
        self.hideturtle()
    
    def create_turtles(screen, n = 10):
        for i in range(n):
            MyTurtle(screen)
    
    def move_turtles(screen, dist=10, angle = 4):
        for i, turtle in enumerate(screen.turtles()):
            turtle.left(angle*(1+i))
            turtle.forward(dist)
            x, y = turtle.pos()
            try:
                turtle.color(abs(x), abs(y), abs(x+y))
            except:
                pass
    
writer = MyTurtle()
writer.penup()
writer.goto(0,100)
writer.write("Click Me!", font=("Arial",30), align = "center")
sleep(10)

width = 1000
height = 1000

from drawperlin import *
#import Painter
#import utils
width = 1000
height = 1000
p = Painter.Painter(width, height)
# Allow smooth drawing
p.setRenderHint(p.Antialiasing)
# Draw the background color
p.fillRect(0, 0, width, height, QColor(255,211,155))
# Set the pen color
p.setPen(QPen(QColor(0, 120, 180, 10), 3))
x_i = 500
y_i = 500
length=100
angle=0
x_f = x_i + length*math.cos(math.radians(angle))
y_f = y_i - length*math.sin(math.radians(angle))
x_f = int(x_f)
y_f = int(y_f)
for inc in range(0,500):
    incs = 0
    if inc %5 == 0:incs=incs-3
    p.drawLine(x_i+inc, y_i+inc, x_f-incs, y_f-incs)

v_path = "ZZZ"
 # Save the vector image
save(p, fname=v_path, folder='XXXX/New/')
#p.setPen(QColor(120,120,0))

import turtle
import turtle as t
import time


def draw_rect(t):
    for i in range(0, 4):
        t.forward(100)
        t.right(90)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_circle(t):
    t.circle(50)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_triangle(t):
    t.forward(100)

    for i in range(0, 2):
        t.left(120)
        t.forward(100)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


t=3
draw_triangle(t)

from turtle import *
import turtle as tur
def petal1(t1, r, ang):
    for i in range(2):
        t1.circle(r, ang)
        t1.left(180 - ang)
def flower1(t1, n, r, ang):
    for i in range(n):
        petal1(t1, r, ang)
        t1.left(360.0 / n)
def move(t1, len):
        win = tur.Screen()
        win.bgcolor("cyan")
        t1.pu()
        t1.fd(len)
        t1.pd()
ws = tur.Turtle()
ws.speed(100)
ws.color("pink")
ws.shape("turtle")
move(ws, -150)
ws.begin_fill()
flower1(ws, 7, 50.0, 50.0)
ws.end_fill()
ws.color("blue")
move(ws, 150)
ws.begin_fill()
flower1(ws, 9, 20.0, 60.0)
ws.end_fill()
ws.color("green")
move(ws, 150)
ws.begin_fill()
flower1(ws, 13, 60.0, 40.0)
ws.end_fill()
tur.mainloop()
tur.Screen().exitonclick()
tur.done()

https://onecompiler.com/python/3xngvdswe

from turtle import*

bgcolor('darkblue')
speed(0)
hideturtle()
for i in range(420):
  color('red')
  circle(i)
  color('orange')
  circle(i*0.8)
  right(3)
  forward(3)
done()

"""
H-Tree Fractal using recursion and Turtle Graphics.
Robin Andrews - https://compucademy.net/
"""

import turtle

SPEED = 5
BG_COLOR = "blue"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 3


def draw_line(tur, pos1, pos2):
    # print("Drawing from", pos1, "to", pos2)  # Uncomment for tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])


def recursive_draw(tur, x, y, width, height, count):
    draw_line(
        tur,
        [x + width * 0.25, height // 2 + y],
        [x + width * 0.75, height // 2 + y],
    )
    draw_line(
        tur,
        [x + width * 0.25, (height * 0.5) // 2 + y],
        [x + width * 0.25, (height * 1.5) // 2 + y],
    )
    draw_line(
        tur,
        [x + width * 0.75, (height * 0.5) // 2 + y],
        [x + width * 0.75, (height * 1.5) // 2 + y],
    )

    if count <= 0:  # The base case
        return
    else:  # The recursive step
        count -= 1
        # Top left
        recursive_draw(tur, x, y, width // 2, height // 2, count)
        # Top right
        recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count)
        # Bottom left
        recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count)
        # Bottom right
        recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)


if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle artist (pen) setup
    artist = turtle.Turtle()
    artist.hideturtle()
    artist.pensize(PEN_WIDTH)
    artist.color(PEN_COLOR)
    artist.speed(SPEED)

    # Initial call to recursive draw function
    recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)

    # Every Python Turtle program needs this (or an equivalent) to work correctly.
    turtle.done()

import os
import importlib
import turtle
importlib.reload(turtle)
sc = Screen()
sc.setup(600,600)
image = os.path.expanduser("alien.gif")
sc.register_shape(image)

t = turtle.Turtle()
t.shape(image)
sc.exitonclick()

import time
from turtle import *
import turtle
def recurse(n):
    inc = 0
    if n>0:
        inc = inc+1
        left(10)
        
        if n<100 :
            forward(5)
        if n<200:
            forward(5)    
                
        else:
            forward(5+inc)
        recurse(n-1)

recurse(300)
turtle.exitonclick()

import sys
from turtle import Turtle, Screen

def hilbert_curve(n, turtle, angle=90):
    if n <= 0:
        return

    turtle.left(angle)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.forward(1)
    turtle.right(angle)
    hilbert_curve(n - 1, turtle, angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, angle)
    turtle.right(angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.left(angle)

depth = int(6)
size = 2 ** depth

screen = Screen()
screen.setworldcoordinates(0, 0, size, size)

yertle = Turtle('turtle')
yertle.speed('fastest')
yertle.penup()
yertle.goto(0.5, 0.5)
yertle.pendown()

hilbert_curve(depth, yertle)

yertle.hideturtle()

screen.exitonclick()

def iterative():
    # np being the previous value
    np = 14

    # starts from 2 since the first case is already assumed to known (14)
    # go up to the 100th number
    for n in range(2, 101):
        result = np - 4
        print("%5d" % n, end="")
        print("%12d" % result)
        np = result
    return 0

iterative()

import turtle
tur.bye()
#tur.done()
#tur.clear()
tur.reset()
turtle.done()
tur.clearscreen()
tur.exitonclick()
turtle.exitonclick()
turtle.done()
turtle.reset()

#https://cs111.wellesley.edu/~cs111/archive/cs111_spring15/public_html/notes/lectures/10_turtle_recursion_4up.pdf
    
import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()


#https://runestone.academy/ns/books/published/pythonds/Recursion/pythondsintro-VisualizingRecursion.html
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

from svg_turtle import SvgTurtle


def draw_spiral(t):
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(20):
        d = 50 + i*i*1.5
        t.pencolor(0, 0.05*i, 0)
        t.width(i)
        t.forward(d)
        t.right(144)
    t.end_fill()


def write_file(draw_func, filename, width, height):
    t = SvgTurtle(width, height)
    draw_func(t)
    t.save_as(filename)


def main():
    write_file(draw_spiral, 'example.svg', 500, 500)
    print('Done.')


if __name__ == '__main__':
    main()


!ls *.gif

import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "10.gif"
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()
#turtle.done()
turtle.reset()

turtle.done()
turtle.reset()

https://casual-effects.com/codeheart/turtle/
https://docs.python.org/3/library/turtle.html

%%javascript
// You can find the Turtle API reference here: https://turtletoy.net/syntax
var Canvas = document.getElementById('myChart')

Canvas.setpenopacity(1);

// Global code will be evaluated once.
const turtle = new Turtle();
turtle.penup();
turtle.goto(-50,-20);
turtle.pendown();

// The walk function will be called until it returns false.
function au(x){
x=x+10
return x
}
function walk(i) {
    turtle.forward(106+au(2));
    turtle.right(144+au(2));
    return i < 4;
}

<div id="myChart"></div>

# Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()

If you are using PHP, try adding the following code at the beginning of the php file:

If you are using localhost, try this:

header("Access-Control-Allow-Origin: *");
If you are using external domains such as server, try this:

header("Access-Control-Allow-Origin: http://www.website.com");

turtle.mainloop() aka turtle.Screen().mainloop() Turns control over to tkinter's event loop. Usually, a lack of turtle.Screen().mainloop() (or turtle.Screen().exitonclick(), etc.) will cause the window to close just because the program will end, closing everything. This, or one of its variants, should be the last statement in a turtle graphics program unless the script is run from within Python IDLE -n.

turtle.done() (Does not close window nor reset anything.) A synonym for turtle.mainloop()

turtle.clear() Deletes everything this turtle has drawn (not just the last thing). Otherwise doesn't affect the state of the turtle.

turtle.reset() Does a turtle.clear() and then resets this turtle's state (i.e. direction, position, etc.)

turtle.clearscreen() aka turtle.Screen().clear() Deletes all drawing and all turtles, reseting the window to it's original state.

turtle.resetscreen() aka turtle.Screen().reset() Resets all turtles on the screen to their initial state.

turtle.bye() aka turtle.Screen().bye() Closes the turtle graphics window. I don't see a way to use any turtle graphics commands after this is invoked.

turtle.exitonclick() aka turtle.Screen().exitonclick() After binding the screen click event to do a turtle.Screen().bye() invokes turtle.Screen().mainloop()

It's not clear that you can close and reopen the graphics window from within turtle without dropping down to the tkinter level that underpins turtle (and Zelle's graphics.py)

For purposes of starting a new hand in your blackjack game, I'd guess turtle.reset() or turtle.resetscreen() are your best bet.

import pygame, math

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth):
    fork_angle = 20
    base_len = 10.0
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - fork_angle, depth - 1)
        drawTree(x2, y2, angle + fork_angle, depth - 1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

drawTree(300, 550, -90, 9)
pygame.display.flip()
while True:
    input(pygame.event.wait())
    

reset



