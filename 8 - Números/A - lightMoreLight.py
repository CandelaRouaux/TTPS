from sys import stdin, stdout
from math import sqrt

lights = int(stdin.readline())
while lights != 0:  
    if sqrt(lights).is_integer():
        stdout.write("yes\n")
    else:
        stdout.write("no\n")
    lights = int(stdin.readline())
