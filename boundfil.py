from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys 
sys.setrecursionlimit(10**6) 
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0,500,0,500)
def boundary_fill(x,y, newcolor, bdrcolor):
    currentcolor=glReadPixels(x,y,1.0,1.0,GL_RGB,GL_FLOAT,None)
    if((currentcolor[0][0][0]!=newcolor[0] or currentcolor[0][0][1]!=newcolor[1] or currentcolor[0][0][2]!=newcolor[2] ) and
        (currentcolor[0][0][0]!=bdrcolor[0] or currentcolor[0][0][1]!=bdrcolor[1] or currentcolor[0][0][2]!=bdrcolor[2] )):
        glColor3f(newcolor[0],newcolor[1],newcolor[2])
        glBegin(GL_POINTS)
        glVertex2i(x,y)
        glEnd()
        boundary_fill(x+1,y,newcolor,bdrcolor)
        boundary_fill(x-2,y,newcolor,bdrcolor)
        boundary_fill(x,y+2,newcolor,bdrcolor)
        boundary_fill(x,y-2,newcolor,bdrcolor)
    glFlush()  
def mouse( btn,  state,  x,  y):
    y = 500-y
    if(btn==GLUT_LEFT_BUTTON):
        if(state==GLUT_UP):
            bCol= (1,0,0)
            color= (1,1,0)
            boundary_fill(x,y,color,bCol)
def world():
    glLineWidth(3)
    glPointSize(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(100,100)
    glVertex2i(300,100)
    glVertex2i(300,300)
    glVertex2i(100,300)
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("sample")
    init()
    glutDisplayFunc(world)
    glutMouseFunc(mouse)
    glutMainLoop()
    return 0
main()
