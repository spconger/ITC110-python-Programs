#simple functions

def cube(number):
    myCube = number * number * number
    return myCube

def getInput():
    number = int(input("Enter a number "))
    return number

def printCube(myCube):
    print ("The cube is",myCube)

def main():
    number=getInput()
    myCube=cube(number)
    printCube(myCube)

main()
    
