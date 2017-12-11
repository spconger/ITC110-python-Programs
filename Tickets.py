# if inside of ifs
# town that has a traffic fines
# $5 for each mile above the speed limit
# Maximum fine of $200

# input speed limit
# input the speed they were travelling

# test if speeding
# get the miles over speedlimit
# multiply each mile over by five
# if fine >200 then set to 200

def getSpeedLimit():
    limit = int(input("Enter the speed limit: "))
    return limit

def getSpeed():
    speed = int(input("Enter the speed traveled: "))
    return speed

def determineFine(limit, speed):
    penultyPerMPH=5
    fine =0
    if speed > limit:
        over = speed-limit
        fine = over * penultyPerMPH
        if fine > 200:
            fine=200
    return fine

def ticket(fine):
    if fine > 0:
        print("You owe", fine,"for speeding")
    else:
        print ("thank you for visiting")

        
def main():
    proceed="y"
    while proceed=="y":
        limit = getSpeedLimit()
        speed = getSpeed()
        fine = determineFine(limit, speed)
        ticket(fine)
        proceed=input("Continue y/n")
        proceed=proceed.lower()
        
    
main()










        
                
