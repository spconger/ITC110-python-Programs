#Same program, but methods
#Define array
#get input
#Do the conversion number to word
#output

def setDays():
    dayNames=["Sun","Mon","Tue",
              "Wed", "Thu", "Fri", "Sat"]
    return dayNames

def getDay():
    day = int(input(" Enter a number between 1 and 7 "))
    return day

def getDayName(dayNumber):
    days=setDays()
    dayOfWeek = days[dayNumber-1]
    return dayOfWeek

def printDay(dayName):
    print (dayName)

def main():
    day = getDay()
    weekDay = getDayName(day)
    printDay(weekDay)

main()
    
