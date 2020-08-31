from sys import stdin, stdout

def puntos_articulación():
    count = 0
    visited = [False] * z
    for vertice in adyacentes.keys():
        if (not(visited[vertice])):
            dfsRoot = v
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

while True:
    try:
        adyacentes = {}
        z = int(stdin.readline()[:-1])
        visited = [False] * z
        df_number = [0] * z
        low = [0] * z
        father = [0] * z
        t = []
        count = 0
        result = []
        for x in range(z):
            v = stdin.readline()[:-1].split()
            adyacentes[int(v[0])] = []
            v[1] = v[1][1:-1]
            for i in range(int(v[1])):
                adyacentes[int(v[0])].append(int(v[i+2]))
        puntos_articulación()
        stdin.readline()
        result = sorted(result, key=lambda tup: (tup[0],tup[1]))
        stdout.write(str(len(result))+" critical links\n")
        for i in result:
            stdout.write(str(i[0])+" - "+ str(i[1])+ "\n")
        stdout.write("\n")
    except:
        break