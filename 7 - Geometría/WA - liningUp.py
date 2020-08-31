from sys import stdin, stdout, float_info
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y    

def puntoLinea(n):
    r = 0
    m = [0] * (n)
    for i in range(n-1):
        if(r+2 > n-i+1):
            break
        for j in range(i+1,n):
            if(points[i].x != points[j].x):
                m[j] = ((points[i].y-points[j].y)/(points[i].x-points[j].x))
            else:
                m[j] = float_info.max

        m.sort()   
        t = 0
        for j in range(i+1, n-1): 
            if (abs(m[j]-m[j+1])< float_info.epsilon):
                t += 1
            else:
                if (t > r):
                    r = t
                t = 0
        if (t > r):
            r = t
    return r+2

tp = int(stdin.readline())
stdin.readline()
for y in range(tp-1):
    points = []
    x = stdin.readline()
    while x != "\n":
        x, y = map(float, x.strip().split())
        points.append(Point(x,y))
        x = stdin.readline()
    stdout.write(str(puntoLinea(len(points)))+"\n")
    stdout.write("\n")

points = []  
for x in stdin:
    x, y = map(float, x.strip().split())
    points.append(Point(x,y))
stdout.write(str(puntoLinea(len(points)))+"\n")
