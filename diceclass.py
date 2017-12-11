#First class example
#dice

from random import randrange

class die:
    def __init__(self, sides):
        self.sides=sides
        self.value=1

    def roll(self):
        self.value=randrange(1,self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value=value


def main():
    again="y"
    num=int(input("How many sides "))
    while again=="y":
    
        die1=die(num)
        die1.roll()
        die2=die(num)
        die2.roll()
        print (die1.getValue(),die2.getValue())
        again=input("Enter y to roll again ")

main()
                            
    
    
