from sys import stdin, stdout

def dfs(c1, c2):
    visited[c1] = True
    road = "Z"*10000

    for edge in ady[c1]:
        if(not visited[edge]):
            if(edge == c2):
                return c1[0]+c2[0]
            else:
                dfs_r = dfs(edge, c2)
                if dfs_r != ("Z"*10000):
                    dfs_r = c1[0]+dfs_r
                    if len(road) > len(dfs_r):
                        road = dfs_r
    return road


cases = int(stdin.readline())

for c in range(cases):
    ady = {}
    stdin.readline()
    m, n = map(int, (stdin.readline().strip().split()))
    for x in range(m):
        cities = stdin.readline().strip().split()
        if cities[0] not in ady:
            ady[cities[0]] = []
        ady[cities[0]].append(cities[1])
        if cities[1] not in ady:
            ady[cities[1]] = []
        ady[cities[1]].append(cities[0])
    for x in range(n):
        visited = {}
        for r in ady:
            visited[r] = False
        cities = stdin.readline().strip().split()
        stdout.write(dfs(cities[0], cities[1])+ "\n")
    if (c != cases-1):
        stdout.write("\n")
