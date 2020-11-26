import numpy as np
from math import *
import turtle
import plotly.express as px
import plotly.graph_objects as go


def genPoints(R1, R2, ang, yAng, A, B):
    #3D Torus
    x = (R2 + R1*cos(ang))*(cos(B)*cos(yAng) + sin(A)*sin(B)*sin(yAng)) - R1*cos(A)*sin(B)*sin(ang)
    y = (R2 + R1*cos(ang))*(cos(yAng)*sin(B) - cos(B)*sin(A)*sin(yAng)) + R1*cos(A)*cos(B)*sin(ang)
    z = cos(A)*(R2 + R1*cos(ang))*sin(yAng) + R1*sin(A)*sin(ang)
    #Luminance
    L = cos(yAng)*cos(ang)*sin(B) - cos(A)*cos(ang)*sin(yAng) - sin(A)*sin(ang)+cos(B)*(cos(A)*sin(ang) - cos(ang)*sin(A)*sin(yAng))
    return x,y,z,L


def findClosest(K1, K2, ang, yAng):
    x,y,z,L = genPoints(1,2, radians(ang), radians(yAng), 2, 2)
    x1 = K1 * x / (K2 + z)
    y1 = K1 * y / (K2 + z)
    return x, y, L

def map(raw, myMax, myMin, targMax, targMin):
    return ((targMax - targMin) / (myMax - myMin)) * (raw + 1.5)

turt = turtle.Turtle()
turt.speed(10)


K1 = 10 #distance to viewer
K2 = 5

for i in range(36):
    for j in range(36):
        x, y, L = findClosest(K1, K2, 10*i, 10*j)
        turt.pu()
        turt.setx(x*50)
        turt.sety(y*50)
        size = map(L,3,0,7,0) + 1
        turt.dot(size)
        print(i,j)



turtle.exitonclick()





#
