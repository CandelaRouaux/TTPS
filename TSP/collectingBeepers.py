from sys import stdin, stdout

def dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1] - point2[1])

def tsp (pos, mask):
    if (mask == (2**(m+1))-1):
        return dist(points[pos], points[0])
    else:
        mini = 99999
        for nxt in range(m+1):   
            if (not(mask & (1 << nxt))):  
                value = tsp (nxt, (mask | (1 << nxt))) + dist(points[pos], points[nxt])
                if (value < mini):
                    mini = value
                    posmin = nxt
        return mini


n = int(stdin.readline().strip())
for x in range(n):
    worldx, worldy = [int(y) for y in stdin.readline().strip().split()]
    points = []
    k1, k2 =  [int(y) for y in stdin.readline().strip().split()]   
    points.append((k1,k2))
    m = int(stdin.readline().strip())
    for z in range(m):
        p1, p2 = [int(y) for y in stdin.readline().strip().split()]   
        points.append((p1,p2))
    stdout.write("The shortest path has length " + str(tsp(0, 1)) + "\n")
