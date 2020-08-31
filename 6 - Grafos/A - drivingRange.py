from sys import stdin

def mst ():
    streets.sort(key=lambda street:street[2])
    for street in streets:
        if union_set(street[0], street[1]):
            aristas.append(street[2])

def UFDS (size):
    for x in range(size):
        p.append(x)

def find_set (i):
    if (i==p[i]):
        return i
    else:
        p[i] = find_set(p[i])
        return p[i]

def same_set (i, j):
	return find_set(i) == find_set(j)

def union_set (i, j):
    x = find_set(i)
    y = find_set(j)
    if (x != y):
        p[y] = x
        return True
    else:
        return False

def check ():
    count = 0
    for x in range(N):
        if (x==p[x]):
            count+= 1
    if count > 1:
        return "IMPOSSIBLE"
    else:
        return max(aristas)

N, M = [int(x) for x in stdin.readline().strip().split()]
while N!=0 or M!=0:
    if N==0 or M==0:
        print("IMPOSSIBLE")
    else:
        streets, p, aristas = [], [], []
        UFDS(1000001)
        for x in range(M):
            c1,c2,peso = [int(x) for x in stdin.readline().strip().split()]
            streets.append((c1,c2,peso))
        mst()
        print(check())
    N, M = [int(x) for x in stdin.readline().strip().split()]
