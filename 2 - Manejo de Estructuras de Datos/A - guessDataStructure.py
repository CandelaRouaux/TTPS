import heapq
import sys
for lines in sys.stdin:
    structures = [1,1,1]
    heap =[]
    queue = []
    stack= []
    for x in range (int(lines)):
        line = list(map(int, input().split()))
        if (line[0]==1):
            heapq.heappush(heap,(line[1]*-1))
            queue.append(line[1])
            stack.append(line[1])
        elif(len(stack)!=0):
            if (line[1]!=queue.pop(0)):
                structures[0]=0
            if (line[1]!=stack.pop()):
                structures[1]=0
            if(line[1]!=(heapq.heappop(heap)*-1)):
                structures[2]=0
        else:
            structures=[0,0,0]
    if(structures.count(1)>1):
        print("not sure")
    elif(structures.count(0)==3):
        print("impossible")
    elif(structures[0]==1):
        print("queue")
    elif(structures[1]==1):
        print("stack")
    elif(structures[2]==1):
        print("priority queue")
