#This program calculates how many vans
#are needed for a group
#This uses an if statement
#steve C 10/10/2017

def main():
    #set constants
    group=29
    vanLoad = 8
    #Do an integer division
    vans=group // vanLoad
    print("You will have",vans,"full vans")
    
    #if statement to get remainder
    remainder = group % vanLoad
    if remainder != 0:
        vans= vans + 1
        print ("You will have one van with",remainder, "Passengers")

    print ("You will need", vans, "Vans")

main()
