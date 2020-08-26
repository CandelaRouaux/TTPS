from sys import stdin, stdout
from math import sqrt

def pythagoras(point1, point2):
    return sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))

def tsp (pos, mask):
    if (mask == (2**n)-1):
        return 0, []
    else:
        mini = 99999
        for nxt in range(n):   
            if (not(mask & (1 << nxt))): 
                value, lis = tsp (nxt, (mask | (1 << nxt))) 
                value += pythagoras(com[pos], com[nxt]) + 16
                if (value < mini):
                    mini = value
                    posmin = nxt
                    lismin = lis  
        posminstr = "("+ str(com[posmin][0]) + "," + str(com[posmin][1]) + ")"
        lismin.insert(0,((posminstr, pythagoras(com[pos], com[posmin]) + 16)))
        return mini, lismin

count = 1
n = int(stdin.readline().strip())
while n != 0:
    com = []
    finalResult = 999999
    for x in range(n):
        a, b = [int(y) for y in stdin.readline().strip().split()]
        com.append((a,b))
    stdout.write("**********************************************************\n")
    stdout.write("Network #"+ str(count) + "\n")
    for x in range(n):
        resultv, resultl = tsp(x, 2**x)
        if resultv < finalResult:
            finalResult = resultv
            lis = resultl
            start = x
    strstart =  "("+ str(com[start][0]) + "," + str(com[start][1]) + ")"
    stdout.write("Cable requirement to connect " + strstart + " to " + lis[0][0] + " is {:.2f} feet.\n".format(lis[0][1]))
    for y in range(1, n-1):
        stdout.write("Cable requirement to connect " + lis[y-1][0] + " to " + lis[y][0] + " is {:.2f} feet.\n".format(lis[y][1]))
    stdout.write("Number of feet of cable required is {:.2f}.\n".format(finalResult))
    count +=1
    n = int(stdin.readline().strip())

