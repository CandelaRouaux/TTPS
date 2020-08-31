import sys
excercises = []
pointsPerExcercise = {}
total = 0

def addPoints(score, value):
    if(score not in pointsPerExcercise):
        pointsPerExcercise[score] = value
    else:
        pointsPerExcercise[score] = pointsPerExcercise[score] + value

for score in sys.stdin:
    score = score [0:-1]
    if (score == "-1"):
        for e in excercises:
            total = total + pointsPerExcercise[e]
        print(len(excercises), total)  
        excercises = []
        pointsPerExcercise = {}
        total = 0
    else:
        score = score.split(" ")
        if (score[1] not in excercises):
            if (score[2] == "right"):
                addPoints(score[1],int(score[0]))
                excercises.append(score[1])
            else:
                addPoints(score[1],20)
