from sys import stdin,stdout 

def GCD(a, b):
    if (b==0):
        return a
    return GCD(b, a%b)

tests = int(stdin.readline())
for test in range(tests):
    x = [int(x) for x in stdin.readline().strip().split()]
    stdout.write(str(abs(GCD(x[0],x[1])))+"\n")