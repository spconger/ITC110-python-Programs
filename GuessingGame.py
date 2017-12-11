#guessing game.
#The game gets a random number between 1 and 1000.
#The player gets 10 guesses.
#With each guess the game tells them if
#they are too high or too low or correct.
#They start off with 10 points.
#Each wrong guess subtracts one point.
#When they are done it displays their score and
#asks if they want to play again.
#If they say yes it restarts the game. I
#f not it shows their previous scores and the
#average of those scores and says goodbye. 
#You should break the game into functions.
#It involves for loops, while loops and ifs.
#***************steps*****************
#Get random number
#get a guess
# check if guess is lower, higher or equal to random
#Do 10 times
#Get Score
#Ask if they want to play again
#if yes do game again
#if no exit and give overall score

from random import randrange

def getRandom():
    number = randrange(1,1001)
    return number

def getGuess():
    guess = int(input("Enter a guess between 1 and 1000 "))
    return guess
                
def evaluateGuess(guess,number):
    correct=0
    if guess > number:
        print ("Too high")
    elif guess < number:
        print ("Too low")
    else:
        print ("Got it!")
        correct=1
    return correct

def getScore(number):
    
    score=10
    for i in range(10):
        guess=getGuess()
        correct=evaluateGuess(guess, number)
        if correct==1:
            break
        score=score-1
    return score


def gamePlay():
    scores=[]
    playAgain="y"
    while playAgain=="y":
        number = getRandom()
        #print(number)
        score=getScore(number)
        scores.append(score)
        print("Your score is",score)
        playAgain=input("Do you want to play again? y/n ")
        playAgain=playAgain.lower()
    return scores

def finalScores():
    scores=gamePlay()
    total=0
    average=0
    print ("your scores are: ")
    for item in scores:
        print(item)
        total += item
    average=total/len(scores)
    print ("your average is ", average)
        

def main():
    finalScores()

main()






