from sys import stdin, stdout
DP=[]
prev=[]

def lis (seq, idx):
    if (DP[idx]!=-1):
        return DP[idx]
    DP[idx] = 1; prev[idx] = -1
    for i in range (idx):
        iLis = lis(seq, i)
        if ((seq[i] < seq[idx]) and (DP[idx] < iLis + 1)):
            DP[idx] = iLis + 1
            prev[idx] = i
    return DP[idx]

def cosito (seq, idx):
    if (prev[idx]== -1):
        print(seq[idx])
    else:
        cosito(seq, prev[idx])
        print (seq[idx])


seq = []
stdin.readline()
stdin.readline()
for x in stdin:
    if (x == "\n"):
        lis(seq,len(seq)-1)
        largest = max(DP)
        print("Max hits:", largest)
        cosito(seq, DP.index(largest))
        print()
        seq = []
        prev = []
        DP = []
    else:
        seq.append(int(x))
        DP.append(-1)
        prev.append(0)
lis(seq,len(seq)-1)
largest = max(DP)
print("Max hits:", largest)
cosito(seq, DP.index(largest))
print()