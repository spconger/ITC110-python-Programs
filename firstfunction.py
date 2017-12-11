#functions with passing a value
#and returning values

#define function
def getNumber():
    number=int(input("Enter a number "))
    return number
    
def cube(num):
    myCube=num * num * num
    return myCube

def printResults():
    number=getNumber()
    print("the cube is",cube(number))#calls cube
    

def main():
    printResults()

main()
            
