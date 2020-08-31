from sys import stdin, stdout

#Se puede hacer con conjuntos

def cc():
    numCC = 0
    for v in range(len(nodes)):
        if (not (visited[v])):
            numCC += 1
            dfs(v)
    return numCC

def dfs(v):
    visited[v] = True
    for w in adyacentes[nodes[v]]: 
        if (not(visited[w])):
            dfs(w)


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tests = int(stdin.readline()[:-1])
stdin.readline()
for x in range(tests):
    last = stdin.readline()[:-1]
    position = letters.index(last)
    nodes = letters[:position+1]
    visited = [False] * len(nodes)
    adyacentes ={}
    for letter in nodes:
        adyacentes[letter] = []
    i = stdin.readline()[:-1]
    while (i!= ""):
        adyacentes[i[0]].append(nodes.index(i[1]))
        adyacentes[i[1]].append(nodes.index(i[0]))
        i = stdin.readline()[:-1]
    stdout.write(str(cc())+"\n")
    if (x != tests -1):
        stdout.write("\n")