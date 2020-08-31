from sys import stdin, stdout
from math import sqrt

N = 10000000
def criba():
    for i in range (2, int(sqrt(N))):
        if (isp[i]):
            for j in range(i*i, N, i):
                isp[j] = False


isp = [True] * N
criba()
for line in stdin.readlines():
    x = int(line)
    if (x < 8):
        stdout.write('Impossible.\n')
    else:
        output = ''
        if (x % 2 == 0):
            output = output + '2 2 '
            x = x - 4
        else: 
            output = output + '2 3 '
            x = x - 5
        i=2
        f = True
        while (f and i<= x/2):
            if (isp[i]):
                if (isp[x-i]):
                    output = output + str(i) + ' ' + str(x-i)
                    f = False
            i += 1
        if f:
            stdout.write('Impossible.\n')
        else:
            stdout.write(output+'\n')
        
