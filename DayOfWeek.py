#List a collection of values under one name

def main():
    dayNames=["Sun","Mon","Tue", "Wed", "Thu", "Fri", "Sat"]
    day = int(input(" Enter a number between 1 and 7 "))
    dayOfWeek = dayNames[day-1]
    print(dayOfWeek)

main()
    
    
