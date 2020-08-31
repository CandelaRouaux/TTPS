from sys import stdin, stdout
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y    
    def setx (self, value):
        self.__x = value
    def sety (self, value):
        self.__y = value
    def getx (self):
        return self.__x
    def gety (self):
        return self.__y

    def distance(self, x, y):
        dist = sqrt((x-self.getx())**2 + (y-self.gety())**2)
        return dist

while True:
    try:
        value = list(map(float, (stdin.readline().strip().split())))
        gopher = Point(value[1], value[2])
        dog = Point(value[3], value[4])
        points = []
        for i in range(int(value[0])):
            v =list(map(float, (stdin.readline().strip().split())))
            p = Point(v[0], v[1])
            points.append(p)
        
        ok = False
        if (value[0] != 0):
            for p in points:
                distG = p.distance(gopher.getx(), gopher.gety())
                distD = p.distance(dog.getx(), dog.gety())/2
                if(not ok):
                    if (distD >= distG):
                        ok = True
                        stdout.write('The gopher can escape through the hole at ({},{}).\n'.format("{:1.3f}".format(p.getx()), "{:1.3f}".format(p.gety())))
        if (not ok):
            stdout.write('The gopher cannot escape.\n')
        e = stdin.readline()
    except:
        break