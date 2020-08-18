from sys import stdin, stdout
from math import sqrt

def pythagoras(point1, point2):
    return sqrt(((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2))

def tsp (pos, mask, lis):
    if (mask.count(1) == n):
        return 0
    else:
        mini = 99999
        posmin = 0
        for i in range(n):   
            if (mask[i] == 0): 
                mask2 = mask[::]
                mask2[i]= 1
                lis2 = []
                value = tsp (i, mask2, lis2) + pythagoras(computers[pos], computers[i]) + 16
                if (value < mini):
                    mini = value
                    posmin = i
                    lis3 = lis2    
        lis.append((posmin, pythagoras(computers[pos], computers[posmin]) + 16))
        lis.extend(lis3)  
        return mini

count = 1
n = int(stdin.readline().strip())
while n != 0:
    computers = []
    finalResult = 999999
    for x in range(n):
        a, b = [int(y) for y in stdin.readline().strip().split()]
        computers.append((a,b))
    stdout.write("**********************************************************\n")
    stdout.write("Network #"+ str(count) + "\n")
    for x in range(n):
        l = []
        mask = []
        for r in range(n):
            mask.append(0)
        mask[x] = 1
        result = tsp(x, mask, l)
        if result < finalResult:
            finalResult = result
            lis = l
            start = x
    stdout.write("Cable requirement to connect (" + str(computers[start][0]) + "," + str(computers[start][1]) + ") to (" + str(computers[lis[0][0]][0]) + "," + str(computers[lis[0][0]][1]) + ") is {:.2f} feet.\n".format(lis[0][1]))
    for y in range(1, n-1):
        stdout.write("Cable requirement to connect (" + str(computers[lis[y-1][0]][0]) + "," +  str(computers[lis[y-1][0]][1]) + ") to (" + str(computers[lis[y][0]][0]) + "," + str(computers[lis[y][0]][1]) + ") is {:.2f} feet.\n".format(lis[y][1]))
    stdout.write("Number of feet of cable required is {:.2f}.\n".format(finalResult))
    count +=1
    n = int(stdin.readline().strip())

