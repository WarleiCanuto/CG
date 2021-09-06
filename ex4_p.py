from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import numpy as np

r = 0.2
n = 50
halfpi = math.pi/2
R = 2

def f_paraboloide(u, v):
    #theta = (u*2*math.pi)/(n-1)
    theta = (v*2*math.pi)/(n-1)
    w = ((u*2)/(n-1))
    x = w*math.cos(theta)
    y = w**2
    z = w*math.sin(theta)
    return x, y, z

def cor(t, c1 = np.array([1,0,1]), c2 = np.array([0.3,0,1])):
    return c1 + t*(c2 - c1)

def desenhaParab():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glColor3fv(cor(((i+j))/(n+1)))
            glVertex3fv(f_paraboloide(i,j))
            glVertex3fv(f_paraboloide(i+1,j))
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    desenhaParab()    
    glPopMatrix()
    glutSwapBuffers()
    a += 5
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

#main loop
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Ex4_Paraboloide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()