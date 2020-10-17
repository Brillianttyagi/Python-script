#Von Koch curve
#import libraries
import matplotlib.pyplot as plt
import numpy as np

#define the variables to hold dividing ratio
m, n = 1, 2

#Provide initial line points.
xInit = [10.0, 300.0]
yInit = [100.0, 10.0]

def applySectionalFormula(x, y, xInHere, yInHere):
    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]
    
    #apply sectional formula
    x3 = (x1 * n + x2 * m) / (m + n)
    y3 = (y1 * n + y2 * m) / (m + n)
    x4 = (x1 * m + x2 * n) / (m + n)
    y4 = (y1 * m + y2 * n) / (m + n)
    
    #Check length of each segment
    length = [((y3 - y1) ** 2 + (x3 - x1) ** 2) ** 0.5, ((y3 - y4) ** 2 + (x3 - x4) ** 2) ** 0.5, ((y4 - y2) ** 2 + (x4 - x2) ** 2) ** 0.5]
    #print(length)
    if((x4 - x3) != 0):
        #find the point that makes equilateral triangle from x3, y3 and x4, y4
        m1 = (y4 - y3) / (x4 - x3)
        m2 = (m1 - 3 ** 0.5) / (1 + 3**0.5 * m1)
        m3 = (m1 + 3 ** 0.5) / (1 - 3 ** 0.50 * m1)
        if(int(np.random.random(1) * 1000)%2 == 0):
            #print(int(np.random.random(1) * 100)%2)
            t = m2
            m2 = m3
            m3 = t
        xT = ((y3 - y4 + m2 * x4 - m3 * x3)/ (m2 - m3))
        yT = m2 * (xT - x4) + y4

        #print(((y3 - yT) ** 2 + (x3 - xT) ** 2) ** 0.5)

        count = 1
        for xp in xInHere:
            if((x1 == xp) and (x2 == xInHere[count])) and ((y1 == yInHere[count - 1]) and (y2 == yInHere[count])):
                xInHere.insert(count, x3)
                yInHere.insert(count, y3)
                xInHere.insert(count + 1, xT)
                yInHere.insert(count + 1, yT)
                xInHere.insert(count + 2, x4)
                yInHere.insert(count + 2, y4)
                return(xInHere, yInHere)
            else:
                count+=1

            
    
xPoints, yPoints = applySectionalFormula(xInit, yInit, xInit[:], yInit[:])
xPoint, yPoint = xPoints[:], yPoints[:]
for step in range(15):
    print("Step: ", step)
    plt.plot(xPoint, yPoint)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    xPoint, yPoint = xPoints[:], yPoints[:]
    points = len(xPoints) - 1
    for i in range(points):
        X = [xPoints[i], xPoints[i+1]]
        Y = [yPoints[i], yPoints[i+1]]
        applySectionalFormula(X, Y, xPoint, yPoint)
       
    xPoints, yPoints = xPoint, yPoint

    
    
    
    
    
    
    
    
    
    
    
    
    
