import pygame
import numpy as np
from pygame import color
from scipy.special import gamma
import time

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT  = WINDOW_WIDTH = 700

N = 50
a = 0
b = 0
coinx=np.random.uniform(0,1)
coiny=np.random.uniform(0,1)

coinx = 0.5
coiny = 0.5

z= []

xypos=[]

#print(coinx,coiny)

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius, 1)
    surface.blit(shape_surf, target_rect)




def fact(f):
    return gamma(f+1)


def updateZ():
    global z
    n = len(xypos)
    xval=np.linspace(0,1,N)
    yval=np.linspace(0,1,N)

    xval += (blockSize/WINDOW_WIDTH)/2
    yval += (blockSize/WINDOW_HEIGHT)/2

    xf=np.power(xval,a) * np.power(1-xval,n-a)
    yf=np.power(yval,b) * np.power(1-yval,n-b)
    z =np.outer(xf,yf)
    #print(xval[0], yval[0])

    Cf = (fact(n+1) / ((fact(a)*fact(n-a)))) * (fact(n+1) / ((fact(b)*fact(n-b))))
    z = z * Cf


def main():
    global SCREEN, CLOCK, a,b, gameover, blockSize, n
    pygame.init()
    gameover = False
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    #CLOCK.tick(1)
    n = 0


    while True:
        SCREEN.blit(pygame.Surface(SCREEN.get_size()), (0, 0))
        drawGrid()
        

        if not gameover:
            x = np.random.uniform(0,1,1)
            y = np.random.uniform(0,1,1)
            a=a+1 if x < coinx else a
            b=b+1 if y < coiny else b
            xypos.append((x,y))
            updateZ()
            if n > 100:
                gameover = True
            n += 1
        time.sleep(0.25)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                """             if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                x/=WINDOW_WIDTH
                y/=WINDOW_HEIGHT

                x = np.random.uniform(0,1,1)
                y = np.random.uniform(0,1,1)

                a=a+1 if x<coinx else a
                b=b+1 if y<coiny else b
                xypos.append((x,y))
                updateZ()
                print(len(xypos))
                #print(x,y)
                #dirty.append([a,b])
                #print(z) """

        pygame.display.update()




def drawGrid():
    global z, gameover, blockSize, n
    
    blockSize = WINDOW_HEIGHT//N #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            i, j=x//blockSize, y//blockSize  #this starts indexing from top-left of box.
            rect = pygame.Rect(x, y, blockSize, blockSize)

            
            if len(z) > 0:
                z[z == np.inf] = np.nanmax(z)
                z[z == np.nan] = np.nanmax(z)
                z_standardized=z/np.max(z)
                z_standardized = np.clip(z_standardized,0,np.nanmax(z_standardized))
                
                count = z_standardized[z_standardized > 0.5]
                
                #if count.size <= 2:
                #    gameover = True
                #print(count.size)

                textsurface1 = pygame.font.SysFont('Arial', 30).render('Grids with p > 0.5 = ' + str(count.size) + '; ' +'Iteration = ' + str(n),1, False, (255, 10, 10))
                textsurface2 = pygame.font.SysFont('Arial', 30).render('The brighter a square, the stronger the guess', False, (255, 10, 10))
                #textsurface = pygame.font.SysFont('Arial', 30).render(str(z_standardized.max()), False, (255, 10, 10))

                SCREEN.blit(textsurface1,(0.5,0.5))
                SCREEN.blit(textsurface2,(0.5,740))


                val=z_standardized[i,j] * 255
                col=(val,val,val)
                #if i == (coinx * WINDOW_WIDTH)//blockSize and j == (coiny * WINDOW_WIDTH)//blockSize:
                #    draw_rect_alpha(SCREEN, (255, 0, 0, 200), (x, y, blockSize, blockSize))
                #else:
                    #draw coin with color
                draw_rect_alpha(SCREEN, (val,0,0,255), (x, y, blockSize, blockSize))
                #pygame.draw.rect(SCREEN, col, rect, 0)
    draw_circle_alpha(SCREEN, (255, 255, 255, 180), ((coinx * WINDOW_WIDTH), (coiny * WINDOW_WIDTH)), blockSize)
            
main()
