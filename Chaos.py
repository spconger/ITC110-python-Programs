#This program is chaos program
#in chapter 1
#It shows how chaotic results
#can arise from simple starts
#Steve Conger
#9/28/2017

def main(): #start of the main function block
    print("This program illustrates a chaotic function")
    x=eval(input("Enter a number between 0 and 1 "))
    y=eval(input("Enter the number of loops to do "))
    for i in range(y):
        x = 3.9 * x * (1-x)
        print(i,"\t", x)

main()
