from sys import stdin, stdout

def UFDS (size):
    for x in range(size):
        p.append(x)
        rank.append(0)

def find_set (i):
	return i if (i==p[i]) else find_set(p[i])

def same_set (i, j):
		return find_set(i) == find_set(j)

def union_set (i, j):
    if (not (same_set(i, j))):
        x = find_set(i)
        y = find_set(j)
        if (rank[x] > rank[y]):
            p[y] = x
        else:
            p[x] = y
            if (rank[x] == rank[y]):
                rank[y]+= 1

def check ():
    s = set()
    for x in range(n):
        s.add(find_set(x))
    return len(s)
        
n,m = map(int,(stdin.readline()[:-1]).split())
count = 1
while (m!=0)or(n!=0):    
    p = []
    rank = []
    UFDS(n)
    for x in range(m):
       i,j = map(int,(stdin.readline()[:-1]).split()) 
       union_set(i-1,j-1)
    stdout.write(("Case {}: " + str(check())+ "\n").format(count))
    count += 1
    n,m = map(int,(stdin.readline()[:-1]).split())