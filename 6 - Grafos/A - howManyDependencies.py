from sys import stdin, stdout

def maximo():
    maxi = -1
    for elem in dic:
        lis = set()
        x = dfs(elem, lis)
        if maxi < x:
            maxi = x
            r = elem
    return r

def dfs(v, lis):
    if v in dic:
        for w in dic[v]: 
            if w not in DP:
                dfs(w, lis)
            else:
                lis.update(DP[w])
            lis.add(w)
        DP[v] = set(lis)
    return len(lis)

n = int(stdin.readline())
while n!=0:
    DP = {}
    dic = {}
    for y in range(1,n+1):
        elem = [int(x) for x in stdin.readline().strip().split()]
        if elem[0] != 0:
            dic[y]= elem[1:]
    stdout.write(str(maximo())+"\n")           
    n = int(stdin.readline())
