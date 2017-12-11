#Grade scores between 100 and 0
#broken into 4 point system

def getScore():
    score=int(input("enter the test score "))
    return score

def getGrade(score):
    grade = 0.0
    if score >= 90:
        grade = 4.0
    elif score >= 85:
        grade = 3.5
    elif score >= 80:
        grade=3.0
    elif score >= 75:
        grade = 2.5
    elif score >= 70:
        grade = 2.0
    elif score >= 65:
        grade = 1.0
    else:
        grade= 0.0
    return grade

def printGrade(grade):
    print ("Your test grade is ", grade)

def main():
    testScore = getScore()
    #print(testScore)
    gradePoint = getGrade(testScore)
    printGrade(gradePoint)


main()




    


    
    
