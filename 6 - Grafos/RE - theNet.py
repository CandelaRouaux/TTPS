from sys import stdin, stdout

def BFS(nodoInicial, nodoFinal):
    cola = []
    distancias = []
    for i in range(int(n)+1):
        distancias.append([int(n),0])
    cola.append(nodoInicial)
    distancias[nodoInicial][0] = 0
    while(len (cola)!= 0):
        t = cola.pop(0)
        for w in dic[t]:
            if (distancias[w][0]==int(n)): 
                distancias[w][0] = distancias[t][0]+1
                distancias[w][1] = t
                cola.append(w) 
    return distancias

n = stdin.readline().strip()
while n!="":
    dic = {}
    for x in range(int(n)):
        v = (stdin.readline().strip().split('-'))
        if (v[1]!=""):
            dic[int(v[0])] = list(map(int, v[1].split(",")))
        else:
            dic[int(v[0])] = []
    z = int(stdin.readline().strip())
    stdout.write("-----\n")
    for x in range(z):
        v = stdin.readline().strip().split()
        dist = BFS(int(v[0]), int(v[1]))
        pos = int(v[1])
        if (dist[pos][0] != int(n)):  
            result = str(pos)
            for x in range(dist[pos][0]):
                pos = dist[pos][1]
                result = str(pos)+" "+result
            stdout.write(result+"\n")
        else:
            stdout.write("connection impossible\n")
    n = stdin.readline().strip()