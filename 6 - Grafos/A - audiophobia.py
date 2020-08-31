from sys import stdin, stdout

def mst ():
    streets.sort(key=lambda street:street[2])
    for street in streets:
        if union_set(street[0], street[1]):
            aristas[street[0]].append((street[1], street[2]))
            aristas[street[1]].append((street[0], street[2]))

def UFDS (size):
    for x in range(size+1):
        p.append(x)

def find_set (i):
	return i if (i==p[i]) else find_set(p[i])

def same_set (i, j):
		return find_set(i) == find_set(j)

def union_set (i, j):
    if (not (same_set(i, j))):
        x = find_set(i)
        y = find_set(j)
        if (x != y):
            p[y] = x
            return True
        else:
            return False

def dfs(c1, c2):
    max_decibels = -1

    dfs_v[c1] = True

    for edge in aristas[c1]:
    	if(not dfs_v[edge[0]]):
    		if(edge[0] == c2):
    			return edge[1]
    		else:
    			dfs_r = dfs(edge[0], c2)
    			if(dfs_r != -1):
    				max_decibels = max(max_decibels, max(dfs_r, edge[1]))

    return max_decibels

C, S, Q = map(int, stdin.readline()[:-1].split())
r = 1
while (C!=0) or (S!=0) or (Q!=0):
    streets = []
    p = []
    UFDS(C)
    aristas = [[] for _ in range(C+1)]
    for street in range(S):
        c1, c2, d = map(int, stdin.readline()[:-1].split())
        streets.append((c1,c2,d))
    
    mst()
    stdout.write("Case #{}\n".format(r))
    for x in range(Q):
        c1, c2 = map(int, stdin.readline()[:-1].split())
        dfs_v = [False] * (C+1)
        j = dfs(c1,c2)
        if (j != -1):
            stdout.write(str(j)+"\n")
        else:
            stdout.write("no path\n")
    r += 1
    C, S, Q = map(int, stdin.readline()[:-1].split())
    if ((C!=0) and (S!=0) and (Q!=0)):
        stdout.write("\n")