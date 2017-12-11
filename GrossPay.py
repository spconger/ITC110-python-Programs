#peer execise 6
#Wages with overtime

def getWage():
    rate = float(input("Enter your hourly rate"))
    return rate

def getHours():
    hours = float(input("Enter your weekly hours"))
    return hours

def calculateGross(rate, hours):
    gross=0
    overtimeRate=1.5
    regHours=40
    if hours > regHours:
        gross=rate * (regHours + ((hours-regHours)*overtimeRate))
    else:
        gross=rate * hours
    return gross

def printGross(gross):
    print("Your gross pay is",gross)

def main():
    rate = getWage()
    hours = getHours()
    gross=calculateGross(rate, hours)
    printGross(gross)


main()
    
    

