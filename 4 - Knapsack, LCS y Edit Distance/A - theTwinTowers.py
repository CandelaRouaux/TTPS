def LCS(s, t):
    n = len(s) + 1
    m = len(t) + 1
    memo = {}
    for i in range(n):
        memo[i,0] = 0
    for j in range(m):
        memo[0,j] = 0
    for i in range(1,n):
        for j in range(1,m):
            if(s[i-1] == t[j-1]):
                memo[i,j] = memo[i-1,j-1] + 1
            else:
                memo[i,j] = max(memo[i-1,j], memo[i,j-1])
    return memo[n-1,m-1]

n1, n2 = map(int, input().split())
num = 1
while(n1!=0)or(n2!=0):
    tower1 = list(map(int,input().split()))
    tower2 = list(map(int,input().split()))
    print("Twin Towers #{}".format(num))
    print("Number of Tiles :",LCS(tower1,tower2))
    print()
    n1, n2 = map(int, input().split())
    num += 1
