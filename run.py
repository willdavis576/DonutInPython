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

xList = np.array([])
yList = np.array([])
zList = np.array([])
LList = np.array([])

for i in range(0, 120):
    for j in range(0,120):
        x,y,z,L = genPoints(1,2, radians(3*i), radians(3*j), 1,1) #get torus coords, 0 -> 2pi. using 120 and scaling to have less processing power
        xList = np.append(xList, x)
        yList = np.append(yList, y)
        zList = np.append(zList, z)
        LList = np.append(LList, L)


data = [go.Scatter3d(x=xList, y=yList, z=zList,mode='markers', marker=dict(size=1, color=LList))]
fig = go.Figure(data=data)
fig.show()


#find pixels closest to screen
K1 = 10 #distance to viewer
K2 = 10 #ditto

xView = np.array([]) #draw on 2D screen
yView = np.array([])

def findClosest(K1, K2, xList, yList, zList, xView, yView):
    for i in range(len(xList)):
        xView = np.append(xView, (K1*xList[i]) / (K2 + zList[i]))
        yView = np.append(yView, (K1*yList[i]) / (K2 + zList[i]))
    return xView, yView

xView, yView = findClosest(K1,K2,xList,yList,zList,xView,yView)
fig = px.scatter(x=xView, y=yView) #2D Drawing
# fig.show()








'''
TURTLEEEEEEEEEE
'''
#
# xTurt = turtle.Turtle()
# xTurt.speed(10)
#
# def dot(Turt, x, y):
#     Turt.pu()
#     Turt.setx(x)
#     Turt.sety(y)
#     Turt.dot(5)
#
#
# for i in range(len(xView)):
#     dot(xTurt, xView[i]*50, yView[i]*50)



















#
