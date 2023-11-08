from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import threading
from math import*

corda = (.1,.1)
cordb = (.1,.5)
cordc = (.4,.5)

def transformation():
    global corda
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-1,0)
    glVertex2f(1,0)
    glEnd()
    
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex2f(0,-1)
    glVertex2f(0,1)
    glEnd()
    
    glColor3f(0, 0, 1)
    glPointSize(10)
    glLineWidth(10)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(*corda)
    glVertex2f(*cordb)
    glVertex2f(*cordc)
    
    glEnd()
    glLineWidth(1)
    glFlush()

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    transformation()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800,800)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("2d transformation ")
glutDisplayFunc(showscreen)

def a():
    glutMainLoop()

t1 = threading.Thread(target=a, args=())
t1.start()

while 1:
    print("Please Choose an option to proceed : \n1.translate\n2.rotate\n3.scaling\n4.reflection\n")
    option = int(input())
    if option == 1:  #trans
        
        tx =  float(input("Enter translation in x :"))
        ty =  float(input("Enter translation in Y :"))
        corda = (corda[0]+tx,corda[1]+ty)
        cordb = (cordb[0]+tx,cordb[1]+ty)
        cordc = (cordc[0]+tx,cordc[1]+ty)
        transformation()
        
    elif option == 2: #rotation
        theta =  float(input("Enter theata :"))
        corda = (corda[0]*cos(theta)-corda[1]*sin(theta),corda[0]*sin(theta)+corda[1]*cos(theta))
        cordb = (cordb[0]*cos(theta)-cordb[1]*sin(theta),cordb[0]*sin(theta)+cordb[1]*cos(theta))
        cordc = (cordc[0]*cos(theta)-cordc[1]*sin(theta),cordc[0]*sin(theta)+cordc[1]*cos(theta))
        transformation()
    elif option == 3: #scaling
        tx =  float(input("Enter scaling in x :"))
        ty =  float(input("Enter scaling in Y :"))
        corda = (corda[0]*tx,corda[1]*ty)
        cordb = (cordb[0]*tx,cordb[1]*ty)
        cordc = (cordc[0]*tx,cordc[1]*ty)
        transformation()
    elif option == 4: # reflection
        opt=int(input("choose your refection \n1.x \n2.y \n3.x&y"))
        if opt == 1:
            corda = (corda[0],-corda[1])
            cordb = (cordb[0],-cordb[1])
            cordc = (cordc[0],-cordc[1])
            dotransformation()
        elif opt == 2:
            corda = (-corda[0],corda[1])
            cordb = (-cordb[0],cordb[1])
            cordc = (-cordc[0],cordc[1])
            dotransformation()
        elif opt == 3:
            corda = (-corda[0],-corda[1])
            cordb = (-cordb[0],-cordb[1])
            cordc = (-cordc[0],-cordc[1])
            transformation()
        
    else :
        print("you have written a wrong input. Please try again")

