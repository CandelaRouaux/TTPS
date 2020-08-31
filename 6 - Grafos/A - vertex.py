from sys import stdin, stdout

MAX_VERTEX = 110

def dfs(v):
    if v in adyacentes:
        for w in adyacentes[v]: 
            if (not(visited[w])):
                visited[w] = True
                dfs(w)

def inaccessibles():
    r = ""
    cant = 0
    for x in range(1,n+1):
        if (not(visited[x])):
            r += " " + str(x)
            cant += 1
    stdout.write(str(cant) + r + "\n")
        
n = int(stdin.readline()[:-1])
while (n != 0): 
    adyacentes= {}
    line = stdin.readline()[:-1]
    while (line !="0"):
        line = list(map(int,(line.split())[:-1]))
        adyacentes[line[0]]= line[1:]
        line = stdin.readline()[:-1]
    check = stdin.readline()[:-1]
    check = list(map(int,check.split()))
    for x in range(1, check[0]+1):
        visited = [False] * MAX_VERTEX 
        dfs(check[x])
        inaccessibles()
    n = int(stdin.readline()[:-1])



