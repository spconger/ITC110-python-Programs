from CardClass import Card
import random

class Deck:
    def __init__(self):
        self.suits=["d","h","c","s"]
        self.cards=[]
       
        
        
    def initializeDeck(self):
        for i in range(1,4):
            suit=self.suits[i]
            for x in range(1,13):
                rank=x
                c=Card(rank,suit)
                self.cards.append(c)
                
    def getDeck(self):
        return self.cards

    def shuffleDeck(self):
        randDeck=self.getDeck()
        random.shuffle(randDeck)
        return randDeck

    def deal(self,number):
        self.newDeck=self.shuffleDeck()
        self.hand=[]
        if number > len(self.newDeck):
            for i in range(number):
                self.hand.append(self.newDeck[i])
                self.newDeck.remove(i)
        return self.hand


    from Deck import Deck
    d = Deck()
    d.initializeDeck()
    hand=d.deal(5)
    print (hand)
                             
        
