from sys import stdin, stdout

def tsp (pos, mask):
    if (mask == ((1 << P) - 1)):
        return - dist[operas[pos][0]][0]
    elif (memo[pos][mask] != 1e8):
        return memo[pos][mask]
    else:
        ans = - dist[operas[pos][0]][0] 
        for nxt in range(P):  
            if (not(mask & (1 << nxt))):  
                ans = max(ans, operas[nxt][1] - dist[operas[pos][0]][operas[nxt][0]] + tsp(nxt, mask | (1 << nxt)))
        memo[pos][mask] = ans
        return ans

def floyd():
    for a in range(N):
        for b in range(N):
            for c in range(N):
                dist[b][c] = min(dist[b][c], dist[b][a] + dist[a][c])

scenarios = int(stdin.readline().strip())
for sc in range(scenarios):
    stdin.readline()
    N, M = [int(y) for y in stdin.readline().strip().split()]
    N += 1 
    dist = []
    for x in range(N):
        dist.append([])
        for y in range(N):
            if(y == x):
                dist[x].append(0)
            else:
                dist[x].append(1e8)
    for x in range(M):
        s1, s2, d = [float(y) for y in stdin.readline().strip().split()]
        dist[int(s1)][int(s2)] = dist[int(s2)][int(s1)] = min(dist[int(s1)][int(s2)], d)
    floyd()
    P = int(stdin.readline().strip())
    operas = [(0,0)]
    for x in range(P):
        s, p = [float(y) for y in stdin.readline().strip().split()]
        operas.append((int(s), p))
    P += 1
    memo = []
    for x in range(P):
        memo.append([])
        for y in range((1 << P)):
            memo[x].append(1e8)
    result = tsp(0, 1)
    if (result > 0.001):
        stdout.write("Daniel can save ${:.2f}\n".format(result))
    else:
        stdout.write("Don't leave the house\n")