#pylint:disable=W0612
import random

class Player:
    id=0
    name=''
    actions=1
    buys=1
    gold=0
    deck=[]
    hand=[]
    discard=[]
    
    
    def newTurn(self):
        self.actions=1
        self.buys=1
        self.gold=0
        self.newHand()
        
        
    def __init__(self, name):
        self.name=name
        self.actions=1
        self.buys=1
        self.gold=0
        self.deck =['Estate','Estate','Estate','Copper','Copper','Copper','Copper','Copper','Copper','Copper']
        self.id= getId()
        
        
    def newHand(self):
        for i in range(0,5):
            self.drawCard()
            
    
    def drawCard(self):
        if len(self.deck) == 0:
            if len(self.discard) == 0:
                return
            for c in self.discard:
                self.deck.append(c)
            self.discard =[]
        cardIndex = random.choice(range(0, len(self.deck)))
        self.hand.append(self.deck[cardIndex])
        del self.deck[cardIndex]
        
        
    def tryUseCardAsAction(self, cardName):
        if cardName not in self.hand:
            return False
        if self.actions > 1:
            actionResult = activateCard(cardName, self)
            if actionResult == True:
                self.actions = self.actions - 1
                return True
        return False
        
        
    def AddCardToDeck(self, cardName):
        self.deck.append(cardName)
        
    
    def AddCardToHand(self, cardName):
        self.hand.append(cardName)
        
    
    def AddCardToDiscard(self, cardName):
        self.discard.append(cardName)
    
    