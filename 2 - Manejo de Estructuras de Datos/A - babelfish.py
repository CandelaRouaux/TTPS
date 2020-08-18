import sys
dic= {}
word = input()
while (word!=""):
    word = word.split(" ")
    dic[word[1]] = word[0]
    word = input()
for line in sys.stdin:
    line = line [:-1]
    try:
        print(dic[line])
    except KeyError:
        print("eh")
