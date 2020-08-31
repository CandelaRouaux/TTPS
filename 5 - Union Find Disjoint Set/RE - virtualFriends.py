from sys import stdin, stdout

def UFDS(x):
    for v in range(x):
        p.append(v)
        size.append(1)

def find_set(i):
    return i if (i==p[i]) else find_set(p[i])

def same_set(i, j):
		return find_set(i) == find_set(j)

def union_set(i, j):
    if (not (same_set(i, j))):
        x = find_set(i)
        y = find_set(j)
        p[y] = x
        size[x] += size[y]
        return x
    else:
        return find_set(i)
    

tests =int(stdin.readline())
for test in range(tests):
    p = []
    size = []
    people = []
    UFDS(100001)
    friends = int(stdin.readline())
    for bond in range(friends):
        news = stdin.readline().strip().split()
        if news[0] not in people:
            people.append(news[0])
        if news[1] not in people:
            people.append(news[1])
        x = union_set(people.index(news[0]),people.index(news[1]))
        stdout.write(str(size[x])+"\n")