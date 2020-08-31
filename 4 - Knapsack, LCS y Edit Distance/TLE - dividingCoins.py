from sys import stdin, stdout

DP = []
for e in range(102):
    DP.append([0])
    for i in range(25000):
        if e == 0:
            DP[e].append(0)
        else:
            DP[e].append(0)

def mochila (N, K, elem):
    for i in range(1,N):
        for j in range(1,K):
            if (elem[i-1] > j):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], (DP[i-1][j-elem[i-1]] + elem[i-1]))
    return DP[N-1][K-1]

tests = int(stdin.readline())
for test in range(tests):  
    coins = int(stdin.readline())
    elem = [int(x) for x in stdin.readline().strip().split()]
    value = sum(elem)
    result = mochila(coins+1, int(value/2)+1, elem)
    stdout.write(str(abs(result*2-value))+"\n")    
        