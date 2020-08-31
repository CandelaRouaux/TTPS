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
            money[x] += money[y]
            money[y] = 0
        else:
            p[x] = y
            money[y] += money[x]
            money[x] = 0
            if (rank[x] == rank[y]):
                rank[y]+= 1
	

tests = int(stdin.readline())
for x in range(tests):
    p = []
    rank = []
    money = []
    dic = {}
    n,m = map(int, (stdin.readline()[:-1]).split())
    UFDS(n)
    for i in range(n):
        money.append(int(stdin.readline()))
    for y in range(m):
        r,s = map(int, (stdin.readline()[:-1]).split())
        union_set(r,s)
    if (money.count(0)==n):
        stdout.write("POSSIBLE\n")
    else:
        stdout.write("IMPOSSIBLE\n")
