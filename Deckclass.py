#Import the Card and the Random
#classes
from CardClass import Card
import random

class Deck:
    def __init__(self):
        #initialize the suits
        self.suits=["d","h","c","s"]
        #initialize the card list
        self.cards=[]
        #call the initializeDeck method
        self.initializeDeck()
        
        
    def initializeDeck(self):
        #this method populates the cards List
        #with cards
        #loop through the suits
        for i in range(1,4):
            suit=self.suits[i]
            #loop through the ranks
            for x in range(1,13):
                rank=x
                #create a card
                c=Card(rank,suit)
                #add to list of cards
                self.cards.append(c)
                
    def getDeck(self):
        #return a deck
        return self.cards

    def shuffleDeck(self):
        #suffle the deck
        randDeck=self.getDeck()
        random.shuffle(randDeck)
        return randDeck

    def deal(self,number):
        #get a shuffled deck
        self.newDeck=self.shuffleDeck()
        #create an empty list for the hand
        self.hand=[]
        #if there are more cards in the deck
        #than the number requestd
        if number < len(self.newDeck):
            #get that number of cards
            #and put them in the hand list
            for i in range(number):
                self.hand.append(self.newDeck[i])
            #remove those cards from the
                #suffled deck
            for c in self.hand:
                self.newDeck.remove(c)
        #return the hand      
        return self.hand


  
    
                             
        
