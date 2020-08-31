from sys import stdin, stdout

def dijkstra(nodoInicial):
    D = [None] * len(nodes)
    P = [None] * len(nodes)
    seen = [False] * len(nodes)
    for v in range(N+1):
        D[v] = float("inf")
        P[v] = 0
    D[nodoInicial]= 0



tests = int(stdin.readline())
for test in range(tests):
    N, M = [int(x) for x in stdin.readline().strip().split()]
    aristas =[[] for _ in range(N+1)]
    for x in range(M):
        a, b, c = [int(x) for x in stdin.readline().strip().split()]
        aristas[a].append((b,c))
        aristas[b].append((a,c))
    #calcular los dos caminos
    #imprimir
