import sys
DP= []
def build_rsq():
    DP.append(0)
    for x in range (1,(len(string))):
        DP.append(DP[x-1]+(string[x-1]==string[x]))

def rsq(l,r):
    return DP[r-1]-DP[l-1]      
string = sys.stdin.readline()[:-1]
queries = int(sys.stdin.readline())
build_rsq()
for i in range(queries):
    l, r = map(int,sys.stdin.readline().split())
    print(rsq(l,r))


