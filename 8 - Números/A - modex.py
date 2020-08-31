from sys import stdin, stdout

def modpowIter (a, b, c):
    res = 1
    while b != 0:
        if b%2==1:
            res = (res * a)%c
        a = (a*a)%c
        b = b//2

    return res

tests = int(stdin.readline())
for test in range(tests):
    a, b, c = map(int, stdin.readline().strip().split())
    stdout.write(str(modpowIter(a,b,c))+"\n")
stdin.readline()