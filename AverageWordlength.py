#Figure out the average length of a word in a sentence
#Get the sentence
#split sentence into words
#loop through the words and get the lengths
#total the lengths
#divide the total length by the number of words
#print the average

def getSentence():
    sentence=input("Enter a sentence ")
    return sentence

def splitSentence():
    mySentence=getSentence()
    words=mySentence.split()
    return words

def getTotalWordLength():
    words=splitSentence()
    counter=0
    for i in range(0, len(words)):
        counter += len(words[i])
        #counter = counter + len(words[i])
    average=calcAverageWordLength(counter, len(words))
    return average

def calcAverageWordLength(total, sizeOfList):
    average = total/sizeOfList
    return average

def printAverage():
    print("The average word length in your sentence is",getTotalWordLength())

def test():
    #print(getSentence())
    #sentenceWords=splitSentence()
    #for i in range(0, len(sentenceWords)):
        #print(sentenceWords[i])
    #print(getTotalWordLength())
    print(getTotalWordLength())

#test()

def main():
    printAverage()


main()





