from sys import stdin, stdout

def mochila (N, K, elem):
    for j in range(K):
        DP[0][j] = 0
    for i in range(N):
        DP[i][0] = 1
    for i in range(1,N):
        for j in range(1,K):
            if (elem[i-1] > j):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] or (DP[i-1][j-elem[i-1]])
    return DP[N-1][K-1]

tests = int(stdin.readline())
for test in range(tests):
    DP = []
    elem = [int(x) for x in stdin.readline().strip().split()]
    value = sum(elem)
    for e in range(len(elem)+1):
        DP.append([])
        for i in range(int(value/2) + 1):
            DP[e].append(-1)
    if (value%2 == 0) and (mochila(len(elem)+1, int(value/2)+1, elem)):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")