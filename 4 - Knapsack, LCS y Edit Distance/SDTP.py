import sys
def ED(s, t):
    
    for i in range(n):
        memo.append([i])
    for j in range(1,m):
        memo[0].append(j)
    for i in range(1,n):
        for j in range(1, m):
            memo[i].append(min(memo[i-1][j-1] + (s[i-1] != t[j-1]), memo[i-1][j] + 1, memo[i][j-1] + 1))    
    return memo[n-1][m-1]

def recorrido(i,j):
    count = 1
    while (i!=0) and (j!=0):
        if (i == 0):
            operaciones.append("{} Insert {},{}".format(count,i,t[j-1]))
            j -= 1
        elif (j==0):
            operaciones.append("{} Delete {}".format(count,i))
            i -= 1
        else:
            minimo = min(memo[i-1][j-1] + (s[i-1] != t[j-1]), memo[i-1][j] + 1, memo[i][j-1] + 1)
            if minimo == memo[i-1][j-1] + (s[i-1] != t[j-1]):
                operaciones.append("{} Replace {},{}".format(count,i,s[j-1]))
                j -= 1
                i -= 1
            elif minimo == memo[i-1][j] + 1:
                operaciones.append("{} Delete {}".format(count,i))
                i -= 1
            else:
                operaciones.append("{} Insert {},{}".format(count,i,t[j-1]))
                j -= 1
        count = count +1



while True:
    try:
        s = sys.stdin.readline()[:-1]
        t = sys.stdin.readline()[:-1]
        operaciones = []
        memo = []
        n = len(s) + 1
        m = len(t) + 1
        print(ED(s,t))
        recorrido(n,m)
        for x in operaciones:
            print(x)
    except EOFError:
        break