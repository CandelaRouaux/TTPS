from sys import stdin, stdout

def puntos_articulación():
    count = 0
    visited = [False] * (n+1)
    for vertice in adyacentes.keys():
        if (not(visited[vertice])):
            dfsRoot = vertice
            hijosRoot = 0
            count, hijosRoot, dfsRoot =dfs(vertice, count, dfsRoot, hijosRoot)


def dfs(v, count, dfsRoot, hijosRoot):
    visited[v] = True
    df_number[v] = count
    count = count + 1
    low[v] = df_number[v]
    for w in adyacentes[v]: 
        if (not(visited[w])):
            t.append((v,w))
            father[w] = v
            if (v ==dfsRoot):
                hijosRoot = hijosRoot+1
            count, hijosRoot, dfsRoot = dfs(w, count, dfsRoot, hijosRoot)
            if (low[w] > df_number[v]):
                result.append((min(v,w), max(v,w)))
            low[v] = min(low[v], low[w])
        elif (w != father[v]):
            low[v] = min(low[v], df_number[w])
    asd=[count, hijosRoot, count]
    return asd

n = int(stdin.readline())
while (n != 0):
    nodo = {}
    visited = [False] * (n+1)
    df_number = [0] * (n+1)
    low = [0] * (n+1)
    father = [0] * (n+1)
    adyacentes = [int(r) for r in stdin.readline().strip().split()]
    while (adyacentes[0] != 0):
        valor = adyacentes.pop(0)
        for x in adyacentes:
            nodo[x].append(valor)
            nodo[valor].append(x)
        adyacentes = [int(r) for r in stdin.readline().strip().split()]
    stdout.write(str(puntos_articulación())+"\n")
    n = int(stdin.readline())