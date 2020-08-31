from sys import stdin, stdout
from math import sqrt

def get_streets():
    for t in town:
        for r in town:
            d = sqrt(((t[0]-r[0])**2)+((t[1]-r[1])**2))
            if d <= 10:
                dist[town.index(t)].append(d)
            else:
                dist[town.index(t)].append(100000)

def floyd():
    for x in range(towns):
        for y in range(towns):
            for w in range(towns):
                if dist[y][w] > dist[y][x] + dist[x][w]:
                    dist[y][w] = dist[y][x] + dist[x][w]



tests = int(stdin.readline())
for test in range(1,tests+1):
    towns = int(stdin.readline())
    town = []
    dist = [[] for _ in range(102)]
    for location in range(towns):
        x = [int(c) for c in stdin.readline().strip().split()]
        town.append((x[0],x[1]))
        
    get_streets() 
    floyd()
    maxi = 0
    for x in range(towns):
        for i in range(towns):
            maxi = max(dist[x][i], maxi)

    stdout.write("Case #{}\n".format(test))
    if (maxi < 100000):
        stdout.write(str("{}").format("{:1.4f}".format(maxi))+"\n")
    else:
        stdout.write("Send Kurdy\n")
    stdout.write("\n")