import turtle
turtle.tracer(0,0)
larriusdarius=turtle.Turtle() #geometry dash youtuber who spreads wave-carried propaganda
larriusdarius.speed(0)
turtle.colormode(255)
def l(x):
    larriusdarius.left(x)
def f(x):
    larriusdarius.forward(x)
def r(x):
    larriusdarius.right(x)
def c(x):
    larriusdarius.fillcolor(x)# c((r,g,b))
def b():
    larriusdarius.begin_fill()
def e():
    larriusdarius.end_fill()
def d():
    larriusdarius.pendown()
def u():
    larriusdarius.penup()
u()
def sequence (testpointreal, testpointimaginary, zsquaredreal, zsquaredimaginary, iterations):
    x=zsquaredreal**2 - zsquaredimaginary**2 + testpointreal
    y=2*zsquaredreal*zsquaredimaginary + testpointimaginary
    zsquaredreal=x
    zsquaredimaginary=y
    if x**2 + y**2 >4:
        return False
    else:
        if iterations>1:
            return sequence (testpointreal, testpointimaginary, zsquaredreal, zsquaredimaginary, iterations-1)
        else:
            return True
c((0, 0, 0))
print (sequence(2, 2, 0, 0, 50))
def mandelbrot (n, quality):
    for x in range (int(-932/quality), int(932/quality)):
        for y in range (int(-932/quality), 1):
            if sequence (x*quality/466, y*quality/466, 0, 0, n):
                larriusdarius.goto(x*quality+400, y*quality)
                d()
                b()
                for i in range (4):
                    f(quality)
                    r(90)
                u()
                e()
                larriusdarius.goto(x*quality+400, -1*y*quality)
                d()
                b()
                for i in range (4):
                    f(quality)
                    r(90)
                u()
                e()
mandelbrot (100, 5)
turtle.update()
turtle.done()