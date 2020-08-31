from sys import stdin, stdout
from math import sqrt

N = 2**31
def criba():
    for i in range (2, int(sqrt(N))):
        if (isp[i]):
            for j in range(i*i, N, i):
                isp[j] = False


isp = [True] * N
criba()
fact = []

def factores(fact, x):
    i = 2
    while x != 1 and x != 0:
        while (x%i==0):
            fact.append(i)
            x = x/i
        i += 1
        while (not isp[i]):
            i +=1

def cantidad_por_factor(n,x):
    r = 0 
    while (x<= n):
        r = r + (n//x)
        x = x*x
    return r

def calcular(n, m):
    fact = []
    factores(fact, m)
    for x in set(fact):
        if cantidad_por_factor(n,x) < fact.count(x):
            return False
    return True

for line in stdin:   
    n,m = [int(x) for x in line.strip().split()]
    if calcular(n,m):
        stdout.write("{} divides {}!\n".format(m,n))
    else:
        stdout.write("{} does not divide {}!\n".format(m,n))