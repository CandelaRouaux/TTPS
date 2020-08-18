import sys
N, M = map(int, sys.stdin.readline().split())
while (N!=0)or(M!=0):
    jack = set()
    for j in range(N):
        jack.add(int(sys.stdin.readline()))
    counter = 0
    for j in range(M):
        i = int(sys.stdin.readline())
        if i in jack:
            counter = counter + 1
    sys.stdout.write(str(counter) + "\n")
    N, M = map(int, sys.stdin.readline().split())