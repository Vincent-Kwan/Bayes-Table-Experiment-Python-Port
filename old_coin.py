import matplotlib.pyplot as plt
import numpy as np
coinx = int(np.random.uniform(0,1) * 500)
coiny = int(np.random.uniform(0,1) * 500)
coinx = 250
coiny = 250

gameover = False
#THIS IS A WAY OF VECTORIZING FUNCTIONS
updater = lambda x,y: x + y if (x > 0) else x
vfunc = np.vectorize(updater)


def updateScore(points):
    global grids, gameover
    x = int(points[0][0])
    y = int(points[0][1])
    x,y = y,x

    if abs(x - coinx) < 50 and abs(y - coiny) < 50: 
        print('You win')
        gameover = True

    Region1 = np.sum(grids[:x, :y])
    Region2 = np.sum(grids[x+1:, 0:y])
    Region3 = np.sum(grids[0:x, y+1:])
    Region4 = np.sum(grids[x+1:, y+1:])

    if coinx <= x and coiny <= y:
        print("REGION 1")
        print(x,y)
        n = np.count_nonzero(Region1)
        Prob = (Region2 + Region3 + Region4)/n
        copygrid = np.copy(grids[:x,:y])
        print(copygrid.shape)
        grids[:,:] = 0
        grids[:x,:y] = vfunc(copygrid, Prob)    

    if coinx > x and coiny <= y:
        print("REGION 2")
        n = np.count_nonzero(Region2)
        Prob = (Region1 + Region3 + Region4)/n
        copygrid = np.copy(grids[x+1:,0:y])
        grids[:,:] = 0
        grids[x+1:,0:y] = vfunc(copygrid, Prob)

    if coinx <= x and coiny > y: 
        print("REGION 3")
        n = np.count_nonzero(Region3)
        Prob = (Region1 + Region2 + Region4)/n
        copygrid = np.copy(grids[0:x,y+1:])
        grids[:,:] = 0
        grids[0:x,y+1:] = vfunc(copygrid, Prob)

    if coinx > x and coiny > y:
        print("REGION 4")
        print(x,y)
        n = np.count_nonzero(Region4)
        Prob = (Region1 + Region2 + Region3)/n
        copygrid = np.copy(grids[x+1:,y+1:])
        grids[:,:] = 0
        grids[x+1:,y+1:] = vfunc(copygrid, Prob)


grids = np.ones((500,500))
plt.setp(plt.gca(), autoscale_on=False)
def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()


pts = []
while not gameover:
    plt.clf()
    tellme('Click on a point')
    plt.imshow(grids, cmap = 'viridis', interpolation='nearest')
    pts = np.asarray(plt.ginput(1, timeout=-1))
    updateScore(pts)

tellme('You guessed the location of the coin within 50 units.') 
plt.imshow(grids, cmap = 'viridis', interpolation='nearest')
plt.show()

