from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

x0 = -1
xn = 1

y0 = -1
yn = 1

n = 50
dx = (xn - x0)/n
dy = (yn - y0)/n


def f(x,y):
    #return x**2-y**2
    return x**3+y*2

def cor(t, c1 = np.array([1,0,1]), c2 = np.array([0.3,0,1])):
    return c1 + t*(c2 - c1)    

def desenhaSuperficie():
    y = y0
    for i in range(n):
        x = x0
        
        glBegin(GL_TRIANGLE_STRIP)
        
        for j in range(n): 

            glColor3fv(cor(((3*i+j)/4)/(n-1)))
            glVertex3f(x, y, f(x, y))
            glVertex3f(x, y + dy, f(x, y + dy))
            x += dx
        
        glEnd()
        
        y += dy

a = 0
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    #glTranslate(-3, 3, 0)
    glRotatef(-a,1,1,0)
    desenhaSuperficie()
    glPopMatrix()
    '''
    glPushMatrix()
    glTranslate(-3, -3, 0)

    glRotatef(-a,0,0,1)
    desenhaSuperficie()
    glPopMatrix()

    glPushMatrix()
    glTranslate(3, -3, 0)
    glRotatef(-a,0,1,0)
    desenhaSuperficie()
    glPopMatrix()

    glPushMatrix()
    glTranslate(3, 3, 0)
    glRotatef(-a,1,0,0)
    desenhaSuperficie()
    glPopMatrix()
    '''
    glutSwapBuffers()
    
    a += 5
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Superficie")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


