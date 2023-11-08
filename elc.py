import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rx = int(input("Enter semi major axis length: "))
ry = int(input("Enter semi minor axis length: "))
xc = int(input("Enter center x coordinate: "))
yc = int(input("Enter center y coordinate: "))


def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(500.0, -500.0, 500.0, -500.0)
	
def setPixel(xn, yn):
	glBegin(GL_POINTS)
	glVertex2f(xn,yn)
	glEnd()
	
def midpoint():
		
	p = (ry**2)-((rx**2)*ry)+(0.25*(rx**2))
	x = 0
	y = ry
	
		
	setPixel(x+xc, y+yc)
	setPixel(x+xc, -y+yc)
	setPixel(-x+xc, -y+yc)
	setPixel(-x+xc, y+yc)
	
	while ((2*(ry**2)*x)<(2*(rx**2)*y)):
		x=x+1
		if p<0:
			p = p+(2*(ry**2)*x)+(ry**2)
		else:
			y=y-1
			p = p+ (2*(ry**2)*x)-(2*(rx**2)*y)+(ry**2)
		setPixel(x+xc, y+yc)
		setPixel(x+xc, -y+yc)
		setPixel(-x+xc, -y+yc)
		setPixel(-x+xc, y+yc)
	while y>0:
		if p>0:

			p = p -(2*(rx**2)*y)+1+(rx**2)
			y=y-1
		else:
			x=x+1
			y=y-1
			p=p+(2*(ry**2)*x)-(2*(rx**2)*y)+(rx**2)
		setPixel(x+xc, y+yc)
		setPixel(x+xc, -y+yc)
		setPixel(-x+xc, -y+yc)
		setPixel(-x+xc, y+yc)
		
	glFlush()
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(2,0)
	midpoint()
	glutSwapBuffers()	
	
def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	wind = glutCreateWindow("Plot Ellipse")
	glutDisplayFunc(draw)
	#glutIdleFunc(midpoint)
	init()
	glutMainLoop()
	
main()
