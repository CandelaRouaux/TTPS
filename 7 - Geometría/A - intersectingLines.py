from sys import stdin, stdout, float_info
from math import fabs

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

class Segment:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2  
    def setp1 (self, value):
        self.__p1 = value
    def setp2 (self, value):
        self.__p2 = value
    def getp1 (self):
        return self.__p1
    def getp2 (self):
        return self.__p2

class Line:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c  
    def seta (self, value):
        self.__a = value 
    def setb (self, value):
        self.__b = value 
    def setc (self, value):
        self.__c = value
    def geta (self):
        return self.__a
    def getb (self):
        return self.__b  
    def getc (self):
        return self.__c

def point_in_box(p,b1,b2):
    return((p.getx() >= min(b1.getx(),b2.getx())) and (p.getx() <= max(b1.getx(),b2.getx())) and (p.gety() >= min(b1.gety(),b2.gety())) and (p.gety() <= max(b1.gety(),b2.gety())))

def points_to_line(p1, p2, l):
    if (p1.getx() == p2.getx()):
        l.seta(1)
        l.setb(0)
        l.setc(-p1.getx())
    else:
        l.setb(1)
        l.seta(-(p1.gety()-p2.gety())/(p1.getx()-p2.getx()))
        l.setc(-(l.geta() * p1.getx()) - (l.getb() * p1.gety()))

def parallelQ(l1, l2):
    return ((fabs(l1.geta()-l2.geta()) <= float_info.epsilon) and (fabs(l1.getb()-l2.getb()) <= float_info.epsilon))

def same_lineQ(l1, l2):
    return (parallelQ(l1,l2) and (fabs(l1.getc()-l2.getc()) <= float_info.epsilon))

def intersection_point(l1,l2,p):
    p.setx((l2.getb()*l1.getc() - l1.getb()*l2.getc()) / (l2.geta()*l1.getb() - l1.geta()*l2.getb()))
    if (fabs(l1.getb()) > float_info.epsilon):
        p.sety(-(l1.geta()*(p.getx())+ l1.getc()) /l1.getb())
    else:
        p.sety(-(l2.geta()*(p.getx())+ l2.getc()) /l2.getb())

def segments_intersect(s1, s2):
    l1 = Line(0,0,0) 
    l2 = Line(0,0,0)
    p = Point(0,0)
    points_to_line(s1.getp1(), s1.getp2(), l1)
    points_to_line(s2.getp1(), s2.getp2(), l2)
    if (same_lineQ(l1,l2)):
        return("LINE")
    if (parallelQ(l1,l2)):
        return("NONE")
    intersection_point(l1,l2,p)
    return ("POINT " + "{:1.2f}".format(p.getx()) + " " + "{:1.2f}".format(p.gety()))

n = int(stdin.readline())
stdout.write('INTERSECTING LINES OUTPUT\n')
for i in range (n):
    x = list(map(int, (stdin.readline().strip().split())))   
    p1 = Point(x[0], x[1])
    p2 = Point(x[2], x[3])
    s1 = Segment(p1, p2)
    p3 = Point(x[4], x[5])
    p4 = Point(x[6], x[7])
    s2 = Segment(p3,p4)
    stdout.write(segments_intersect(s1,s2)+"\n")
stdout.write('END OF OUTPUT\n')