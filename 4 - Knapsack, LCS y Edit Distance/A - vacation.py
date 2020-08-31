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



seq1 = input()
case = 1 
while (seq1 != "#"):
    seq2= input()
    ans = LCS(seq1,seq2)
    print ("Case #{}: you can visit at most {} cities.".format(case, ans))
    case += 1
    seq1= input()