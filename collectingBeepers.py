from sys import stdin, stdout

def dist(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1] - point2[1])

def tsp (pos, mask):
    if (mask.count(1) == (m+1)):
        return dist(points[pos], points[0])
    else:
        mini = 99999
        posmin = 0
        for i in range(m+1):   
            if (mask[i] == 0): 
                mask2 = mask[::]
                mask2[i]= 1
                value = tsp (i, mask2) + dist(points[pos], points[i])
                if (value < mini):
                    mini = value
                    posmin = i
        return mini


n = int(stdin.readline().strip())
for x in range(n):
    worldx, worldy = [int(y) for y in stdin.readline().strip().split()]
    points = []
    mask = [1]
    k1, k2 =  [int(y) for y in stdin.readline().strip().split()]   
    points.append((k1,k2))
    m = int(stdin.readline().strip())
    for z in range(m):
        p1, p2 =  [int(y) for y in stdin.readline().strip().split()]   
        points.append((p1,p2))
    for w in range(m):
        mask.append(0)
    stdout.write("The shortest path has length " + str(tsp(0, mask)) + "\n")
