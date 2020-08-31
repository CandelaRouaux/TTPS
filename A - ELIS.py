DP=[]
prev=[]

def lis (seq, idx):
    if (DP[idx]!=-1):
        return DP[idx]
    DP[idx] = 1; prev[idx] = -1
    for i in range (idx):
        iLis = lis(seq, i)
        if ((seq[i] < seq[idx]) & (DP[idx] < iLis + 1)):
            DP[idx] = iLis + 1
            prev[idx] = i
    return DP[idx]

x = int (input())
for y in range(x):
    DP.append(-1)
    prev.append(0)
seq = list(map(int, input().split()))
lis(seq,x-1)
print(max(DP))