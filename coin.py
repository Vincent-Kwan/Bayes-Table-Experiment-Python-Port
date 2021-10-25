import matplotlib.pyplot as plt
import numpy as np

n=1000
coinx = int(np.random.uniform()*n)
coiny = int(np.random.uniform()*n)
coinx = int(.5*n)
coiny = int(.5*n)
n2=(n)**2
#THIS IS A WAY OF VECTORIZING FUNCTIONS
p=0.9



def updateScore(points):
    global grids
    x = int(points[0][0])
    y = int(points[0][1])
    #x,y = y,x
    r1 = grids[:x+1, :y+1]
    r2 = grids[x+1:, :y+1]
    r3 = grids[:x+1, y+1:]
    r4 = grids[x+1:, y+1:]
    p1=np.sum(r1)
    p2=np.sum(r2)
    p3=np.sum(r3)
    p4=np.sum(r4)
    #print(p1,p2,p3,p4,p1+p2+p3+p4)
    
    if coinx <= x and coiny <= y:
        Y1=(1-p)/( (1-p)*p1  + (p/3)*p2  + (p/3)*p3  + (p/3)*p4 ) #P(Info Correct | Info incorrect)
        Y2=(p/3)/( (1-p)*p1  + (p/3)*p2  + (p/3)*p3  + (p/3)*p4 )
        Y3=(p/3)/( (1-p)*p1  + (p/3)*p2  + (p/3)*p3  + (p/3)*p4 )
        Y4=(p/3)/( (1-p)*p1  + (p/3)*p2  + (p/3)*p3  + (p/3)*p4 )
        
    elif coinx > x and coiny <= y:
        Y1=(p/3)/( (p/3)*p1  + (1-p)*p2  + (p/3)*p3  + (p/3)*p4 )
        Y2=(1-p)/( (p/3)*p1  + (1-p)*p2  + (p/3)*p3  + (p/3)*p4 )
        Y3=(p/3)/( (p/3)*p1  + (1-p)*p2  + (p/3)*p3  + (p/3)*p4 )
        Y4=(p/3)/( (p/3)*p1  + (1-p)*p2  + (p/3)*p3  + (p/3)*p4 )

    elif coinx <= x and coiny > y: 
        Y1=(p/3)/( (p/3)*p1  + (p/3)*p2  + (1-p)*p3  + (p/3)*p4 )
        Y2=(p/3)/( (p/3)*p1  + (p/3)*p2  + (1-p)*p3  + (p/3)*p4 )
        Y3=(1-p)/( (p/3)*p1  + (p/3)*p2  + (1-p)*p3  + (p/3)*p4 )
        Y4=(p/3)/( (p/3)*p1  + (p/3)*p2  + (1-p)*p3  + (p/3)*p4 )

    elif coinx > x and coiny > y:
        Y1=(p/3)/( (p/3)*p1  + (p/3)*p2  + (p/3)*p3  + (1-p)*p4 )
        Y2=(p/3)/( (p/3)*p1  + (p/3)*p2  + (p/3)*p3  + (1-p)*p4 )
        Y3=(p/3)/( (p/3)*p1  + (p/3)*p2  + (p/3)*p3  + (1-p)*p4 )
        Y4=(1-p)/( (p/3)*p1  + (p/3)*p2  + (p/3)*p3  + (1-p)*p4 )
    
    #print(Y1+Y2+Y3+Y4,'Why is this not 1')
    #print('%.1f %.1f %.1f %.1f'%(Y1,Y2,Y3,Y4))
    #print('%.1f %.1f %.1f %.1f'%(p1,p2,p3,p4))
    r1*=Y1
    r2*=Y2
    r3*=Y3
    r4*=Y4


grids = np.ones((n,n))/n2
plt.setp(plt.gca(), autoscale_on=False)


print(coinx,coiny)
pts = []
while True:
    
    plt.clf()
    
    plt.imshow(grids.T, cmap = 'Blues', interpolation='nearest',origin='upper')
    plt.scatter(coinx,coiny)
    pts = np.asarray(plt.ginput(1, timeout=-1))
    
    updateScore(pts)
    #print(grids.T)
    

