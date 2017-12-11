#simple function

#creating a function
def cube():
    number = int(input("Enter a number "))
    myCube=number * number * number
    print ("the cube is", myCube)

def main():
    cube()#calling it in main

main()
