from sys import stdin, stdout
from functools import reduce 

tests = int(stdin.readline())
for test in range(tests):
    friends, boxes = map(int, stdin.readline().strip().split())
    res = 0
    for box in range(boxes):
        x = [int(n) for n in stdin.readline().strip().split()]
        res = res + reduce(lambda x, y: x*y, x[1:])
    stdout.write(str(res%friends)+ "\n")
