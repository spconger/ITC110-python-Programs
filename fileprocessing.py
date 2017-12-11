#Files

def main():
    fileName=input("Enter File Name")
    inFile = open(fileName, "a")
    content = input("Write Something ")
    print(content, file=inFile)
    inFile.close()

    print("********************")
    inFile = open(fileName,"r")
    text=inFile.read()
    print (text)
    inFile.close()

main()


