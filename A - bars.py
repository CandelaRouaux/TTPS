
DP = []
elem =[]
def mochila (N, K):
    for i in range(N):
        DP[i][0] = 1
    for j in range(K):
        DP[0][j] = 0
    DP[0][0] = 1
    for i in range(1,N):
        for j in range(1,K):
            if (elem[i] > j):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] or (DP[i-1][j-elem[i]])
                
    return DP[N-1][K-1]

tests = int(input())
for test in range(tests):
    DP = []
    elem =[0]
    value = int(input())
    bars = int(input())
    elem.extend(list(map(int, input().split())))
    for bar in range(bars + 1):
        DP.append([])
        for i in range(value + 1):
            DP[bar].append(-1)
    if mochila(bars+1, value+1):
        print("YES")
    else:
        print("NO")