#peer exercise 5

def main():
    mySentence = input("enter a sentence")
    wordList = mySentence.split()
    counter=0
    for i in range(0,len(wordList)):
        wordLength=len(wordList[i])
        #counter=counter + wordLength
        counter += wordLength
    average = counter/len(wordList)
    print ("the average word is ",average,"characters long")

main()
