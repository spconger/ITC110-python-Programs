from Deckclass import Deck

d=Deck()
numberOfHands = 3
for i in range(1, numberOfHands +1):
    hand=d.deal(5)
    for c in hand:
        print("hand " + str(i),c)
       


