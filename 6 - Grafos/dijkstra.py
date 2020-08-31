def dijkstra(nodoInicial):
    D = [None] * len(nodes)
    P = [None] * len(nodes)
    seen = [False] * len(nodes)
    for v in nodes:
        D[v] = float("inf")
        P[v] = 0
    D[nodoInicial]= 0
    for v in nodes:
        queue = [i for i in range(len((nodes))]
        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue: 
                if dist[n] < min_dist and not seen[n]:
                    min_dist = dist[n]
                    u = n

        queue.remove(u)
        seen[u] = True
        for w in ady[u]:
            if not seen[w]:
                if D[w] > (D[u] + c(u,w)): #ver como esta guardado el peso
                    D[w] = D[u] + c(u,w);
                    P[w] = u;