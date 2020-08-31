import sys
def ED(s, t):
    n = len(s) + 1
    m = len(t) + 1
    memo = []
    for i in range(n):
        memo.append([i])
    for j in range(1,m):
        memo[0].append(j)
    for i in range(1,n):
        for j in range(1, m):
            memo[i].append(min(memo[i-1][j-1] + (s[i-1] != t[j-1]), memo[i-1][j] + 1, memo[i][j-1] + 1))
    return memo[n-1][m-1]

tests = int(sys.stdin.readline()[:-1])
for x in range(tests):
    s = sys.stdin.readline()[:-1]
    t = sys.stdin.readline()[:-1]
    if(len (s)== 0):
        sys.stdout.write(str(len(t))+ "\n")
    elif(len (t)== 0):
        sys.stdout.write(str(len(s))+ "\n")
    else:
        sys.stdout.write(str(ED(s,t))+ "\n")
    