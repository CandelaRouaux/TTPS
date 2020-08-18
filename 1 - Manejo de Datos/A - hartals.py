tests = int (input())
for test in range(tests):
    days = []
    for i in range (int (input())):
        days.append(0) 
    for party in range(int (input())):
        hartals = int(input())
        for n in range(hartals-1,len(days),hartals):
            days[n] = days[n] + 1
    hartals = 0
    for day in range(len(days)):
        if((days[day]!=0)and(day%7 != 5)and(day%7 != 6)):
            hartals = hartals + 1
    print (hartals)