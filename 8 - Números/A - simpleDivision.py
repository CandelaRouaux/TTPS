from sys import stdin,stdout 

def GCD(a, b):
    if (b==0):
        return a
    return GCD(b, a%b)

n = stdin.readline().strip()
while n!= "0":
    n = [int(x) for x in n[:-2].split()]
    result = n[1] - n[0]
    for i in n[2:]:
        result = GCD(result, i-n[0])
    stdout.write(str(abs(result))+"\n")
    n = stdin.readline().strip()
