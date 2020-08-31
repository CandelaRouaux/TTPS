from sys import stdin, stdout
from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y    

def find_closest(p):
    if len(p)==1:
        return 10000
    else:
        L = len(p)//2  
        l_value = p[len(p)//2].x
        min1 = find_closest(p[:L])
        min2 = find_closest(p[L:])
        mini = min(min1,min2)
        points_in_range_x = list(filter(lambda point: point.x>(l_value-mini) and point.x<(l_value+mini), p))
        for p1 in points_in_range_x:
            points_in_range_y = list(filter(lambda point: point.y>(p1.y-mini) and point.y<(p1.y+mini), points_in_range_x))
            for p2 in points_in_range_y:
                if(p1 != p2):
                    dist = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
                    mini = min(mini, dist)
        return mini


n = int(stdin.readline())

while (n != 0):
    points = []
    for i in range(n):
        x, y = map(float, stdin.readline().strip().split())
        points.append(Point(x,y))

    points.sort(key=lambda point:point.x)
    r = find_closest(points)
    if (r >= 10000):
        stdout.write('INFINITY\n')
    else:
        stdout.write("{}\n".format("{:1.4f}".format(r)))

    n = int(stdin.readline())