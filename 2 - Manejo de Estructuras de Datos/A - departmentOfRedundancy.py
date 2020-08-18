import sys
seq = []
for lines in sys.stdin:
    seq.extend(list(map(int,lines.split())))
dic = {}
for element in seq:
    try:
        dic[element] = dic[element] + 1
    except KeyError:
        dic[element] = 1
for x in dic:
    print(x, dic[x])