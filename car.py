from OpenGL.GL import *
from OpenGL.GL import *
from OpenGL.GL import *

def init():
    glClearColor(0.0,0.0,0.0,0.1)
    gluOrtho2D(-400,400,-400,400)

def rock():
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(-200,0)
    glVertex2f(-250,-10)
    glVertex2f(-100,50)
    glVertex2f(-150,-20)
    glEnd()
    glFlush()
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE| GLUT_RGBA)
    glutCreateWindowSize(800,800)
    glutDisplayFunc(rock)
    init()
    glutMainLoop()
    
main()