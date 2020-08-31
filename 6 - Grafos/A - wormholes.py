from sys import stdin, stdout

def bellmanFord():
    vd = [10000 for _ in range(nm[0]+1)]
    vp = ["" for _ in range(nm[0]+1)]
    vd[0] = 0
    for i in range(len(graphs)-1):
        nodo = 0
        for graph in graphs:
            for x in graph:
                if (vd[nodo] > (vd[x[0]]+x[1])):
                    vd[nodo] = vd[x[0]]+x[1]
                    vp[nodo] = x[0]
            nodo += 1
    nodo = 0
    for graph in graphs:
        for x in graph:
            if (vd[nodo] > (vd[x[0]]+x[1])):
                return True
        nodo += 1
    return False

cases = int(stdin.readline())
for c in range(cases):
    graphs = []
    nm = list(map(int, (stdin.readline().strip().split())))
    for x in range(nm[0]):
        graphs.append([])
    for x in range(nm[1]):
        xyt = list(map(int, (stdin.readline().strip().split())))
        graphs[xyt[0]].append((xyt[1], xyt[2]))
    if (bellmanFord()):
        stdout.write('possible\n')
    else:
        stdout.write('not possible\n')
