from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (0,0,1),(0.2,0.2,1),(0.4,0.4,1),(0.6,0.6,1),(0.8,0.8,1),(0.9,0.1,1),(0.8,0.2,1),(0.4,0.3,1) )
quadro = 0

def desenha():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(quadro,1,1,0)
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    raio = 0.5
    glVertex3f(0,0,0)
    for i in range(0,6+7):
        a = (i/6) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,y, 0)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    raio = 0.5
    glVertex3f(0,0,1)
    for i in range(0,6+7):
        a = (i/6) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,y, 1)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor3fv(cores[0])
    raio = 0.5
 
    for i in range(0,6+7):
        a = (i/6) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
 
        glVertex3f(x,y, 0)
        glVertex3f(x,y, 1)
        
        b = (i+1/6) * 2 * math.pi
        x2 = raio * math.cos(a)
        y2 = raio * math.sin(a)
        glVertex3f(x2,y2, 0)
        glVertex3f(x2,y2, 1)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()
    quadro += 5

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

#main loop
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Prism")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
#glutTimerFunc(50,timer,1)
glutMainLoop()


