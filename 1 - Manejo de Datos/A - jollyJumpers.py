import sys
for lines in sys.stdin:
    lines = lines.strip().split()
    numbers = set()
    ok = True
    for elem in range(len(lines)-1):
        x =abs(int(lines[elem])-int(lines[elem+1]))
        if (x < len(lines)):
           numbers.add(x)
    for x in (range(1,(len(lines)-1))):
        if (x not in numbers):
            ok = False
    if (ok):
        print ("Jolly")
    else:
        print ("Not jolly")
