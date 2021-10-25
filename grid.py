import pygame
import numpy as np
import math
from scipy.special import gamma
#initiliazation of variables

N = 100
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
trial = 1 #trial number
#z = np.random.uniform(0,1,N**2).reshape(N,N)

def fact(n):
    #return math.factorial(n)
    return gamma(n+1)

def jointf(pos, n):
    global N
    a = pos[0]
    b = pos[1]
    x = np.linspace(0,1,N)
    y = np.linspace(0,1,N)
    xf = np.power(x,a) * np.power(1-x,n-a) 
    yf = np.power(y,b) * np.power(1-y,n-b) 
    print(xf)
    print(yf)
    return np.outer(xf,yf)

def Cf(x, y, n):
    v = ((fact(n+1)) / (fact(x) * fact(n-x) * fact(y) *fact(n-y)))*fact(n+1)
    return v


n = 5
xy = np.array([0.5,0.5]) #initial coin position
xy2 = np.random.uniform(0,1,2*n).reshape((n,2))



                  
#
xpos = np.cumsum(xy2[:,0] < xy[0])
ypos = np.cumsum(xy2[:,1] < xy[1])
#print(xpos, ypos)
xpos = np.array([0,0,1,1,1,2,2,3,3,3,4,5,5,5,5,5,5,5,6,6,6,7,7,7,7,7,7,8,8,9])
ypos = np.array([1,2,3,4,5,5,6,7,8,9,10,10,11,12,13,14,15,16,17,18,19,20,20,21,22,23,24,25,25,26])

xypos = np.stack((xpos,ypos),axis=1)
#print(xypos)

z=None

def updateZ():
    global trial, z
    
    t1=jointf(xypos[trial,:],trial)
    #t2= Cf(xpos[trial], ypos[trial], trial)
    #print(np.max(t1),np.max(t2))

    z= t1#*t2
    print(np.max(z),np.sum(z))
    trial += 1
    #z=z/np.max(z) No hack
updateZ()

#for i in range(n):
#    z=jointf(xypos[i,:],i)







def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                updateZ()
                x,y=pygame.mouse.get_pos()

        pygame.display.update()


    


def drawGrid():
    global z
    blockSize = WINDOW_HEIGHT//N #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            i,j = x//blockSize, y//blockSize
            rect = pygame.Rect(x, y, blockSize, blockSize)
            rect2 = pygame.Rect(WINDOW_HEIGHT//2,WINDOW_HEIGHT//2, blockSize, blockSize)
            v=z[i,j]*255
            
            pygame.draw.rect(SCREEN, (00,00,255), rect2, 1)
            pygame.draw.rect(SCREEN, (v,v,v), rect, 0)
            


main()