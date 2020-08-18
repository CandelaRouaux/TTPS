tests = int (input())
for test in range(tests):
    input()
    order = list(map(int,input().split()))
    grades = order[:]
    grades.sort(reverse=True)
    counter = 0
    for elem in range(len(order)):
        if order[elem]==grades[elem]:
            counter += 1
    print(counter)
