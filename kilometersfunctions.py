#conversion to kilometers
#get the input in miles
#calculation miles * 1.609
#print out results

def getMiles():
    miles=float(input("enter the miles "))
    return miles

def convert(m):
    kilometers=m * 1.609
    return kilometers

def printKilometers(k):
    print (k)

def main():
    mls = getMiles()
    ks = convert(mls)
    printKilometers(ks)

main()
