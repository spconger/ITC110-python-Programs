#using functions
# this program uses a function
#to gather some text
#another to write it to a file
#another to read the file
#and a main function to call
#the functions
#steve conger 10/12/2017

# function to get text
def getText():
    myText=input("enter your text ")
    return myText #returns the text
                  #to the callling function

def writeFile():
    text=getText() #calls getText() assigns
                   #returned value
    #get filename
    fname=input("enter file name")
    #open a file for writing
    outfile=open(fname,"w")
    #print the text to the file
    print(text, file=outfile)

def readFile():
    #gets file name
    fname=input("enter file name")
    #opens the file for reading
    infile=open(fname,"r")
    #reads what's in the file
    data = infile.read()
    #prints output
    print(data)

def main():
    writeFile() #calls writeFile()
    #no need to call getText() because
    #it is called in writeFile()
    #this is just for seperation
    print("**********************")
    readFile() #call readFile()

main()#call main
