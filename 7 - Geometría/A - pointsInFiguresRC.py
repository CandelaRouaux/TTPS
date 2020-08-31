from sys import stdin, stdout
from math import sqrt

class Rectangle():
    def __init__(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
    
    def point_in_figure(self, x, y):
        return((x > min(self.__x1,self.__x2)) and (x < max(self.__x1,self.__x2)) and (y > min(self.__y1,self.__y2)) and (y < max(self.__y1,self.__y2)))

class Circle():
    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__r = r
    
    def point_in_figure(self, x, y):
        dist = sqrt((x-self.__x)**2 + (y-self.__y)**2)
        return (dist < self.__r)

f = stdin.readline()
figures = []
while (f != '*\n'):
    f = f.strip().split()
    if (f[0] == 'r'):
        r = Rectangle(float(f[1]), float(f[3]), float(f[2]), float(f[4]))
        figures.append(r)
    else:
        c = Circle(float(f[1]), float(f[2]), float(f[3]))
        figures.append(c)
    f = stdin.readline()

p = stdin.readline().strip().split()
count = 1
while (p[0] != p[1]) or (p[0] != '9999.9'):
    ok = True
    for f in figures:
        if (f.point_in_figure(float(p[0]), float(p[1]))):
            stdout.write('Point {} is contained in figure {}\n'.format(count, (figures.index(f)+1)))
            ok = False
    if ok: 
        stdout.write('Point {} is not contained in any figure\n'.format(count))
    count = count + 1
    p = stdin.readline().strip().split()
