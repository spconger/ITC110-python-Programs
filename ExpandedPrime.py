#Code will generate 41 prime number

def getNumber():
    number = int(input("Enter a number between 0 to 40: "))
    return number

def checkNumber(number):
    checkedNumber=0
    if number >=0 and number <=40:
        checkedNumber = number
    else:
        checkedNumber=-1
    return checkedNumber
    
        
def getPrime(number):
    prime = number * number - number +41
    return prime

def printPrime(prime):
    print ("The prime number is", prime)

def main():
    num = getNumber()
    checkNum = checkNumber(num)
    #print(checkNum)
    if checkNum == -1:
        print ("Numbers must be between 0 and 40")
        return
    prime = getPrime(num)
    printPrime(prime)

main()








        
