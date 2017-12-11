#miles per gallon
# as class

class Mileage:
    def __init__(self, miles, gallons):
        self.miles=miles
        self.gallons=gallons
        

    def setMiles(self, miles):
        self.miles=miles

    def mpg(self):
        self.milesPerGallon=self.miles / self.gallons

    def getMPG(self):
        return self.milesPerGallon

    def __str__(self):
        self.mpg()
        return "Your mpg is " + str(self.getMPG())
    

def main():
    mls = float(input("How many total miles "))
    gals = float(input("How many gallons "))
    mileage=Mileage(mls, gals)
    print (mileage)

main()











    
