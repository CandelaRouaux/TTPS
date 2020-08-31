import sys
DP = []
prev = []
elephants = []
num = 1

def cosito (seq, idx):
    if (prev[idx]== -1):
        print(seq[idx][2])
    else:
        cosito (seq, prev[idx])
        print (seq[idx][2])

#def lis (seq):
#    ans = 0
#    for i in range(len(seq)):
#        DP[i] = 1
#        prev[i] = -1
#        for j in range(i):
#           if ((seq[j][2] > seq[i][2]) and (seq[j][1] < seq[i][1]) and (DP[i] < DP[j]+1)):
#                DP[i] = DP[j]+1
#                prev[i] = j
#        if (DP[ans] < DP[i]):
#            ans = i
#    return ans


def lis (seq, idx):
    if (DP[idx] != -1):
        return DP[idx]
    DP[idx] = 1; prev[idx] = -1
    for i in range (idx):
        iLis = lis(seq, i)
        if ((seq[i][1] > seq[idx][1])and(seq[i][0] < seq[idx][0]) and (DP[idx] < iLis + 1)):
            DP[idx] = iLis + 1
            prev[idx] = i
    return DP[idx]

for lines in sys.stdin:
    lines = lines [0:-1]
    a,b = map(int, lines.split(" "))
    elephants.append((a,b,num))
    DP.append(-1)
    prev.append(0)
    num = num + 1
elephants.sort(key=lambda elephant:elephant[0])
lis(elephants, num - 2)
print(max(DP))
cosito(elephants,DP.index(max(DP)))