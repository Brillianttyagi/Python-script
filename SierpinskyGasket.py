#Code of Sierpinsky Gasket
import numpy as np
import matplotlib.pyplot as plt

#define triangle vertices
triangleSides = [[1,1], [3,100], [100, 5]]
#find a new random point inside triangle, set it
midPoint = [5, 7]
points = triangleSides #to prevent modification of original list
#display original traingle points
for side in triangleSides:
    plt.scatter(side[0], side[1])
#display points
plt.show()

#fidne the midpoint between random vertices and repeat
for point in range(1000):
    randomSide = np.random.random(1) #finds the random number in range (0,1)
    randomSide = int(1029 * randomSide) % 3 #apply random integer generation technique
    #find the midpoint between randomSide and current midpoint
    midPoint = [(triangleSides[randomSide][0] + midPoint[0]) / 2, (triangleSides[randomSide][1] + midPoint[1]) / 2]
    points.append(midPoint)
    
    if(point % 50 == 0):
        print('At step ', point)
        for showPoint in range(point):
            plt.scatter(points[showPoint][0], points[showPoint][1])
        plt.show()
            