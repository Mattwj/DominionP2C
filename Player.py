#pylint:disable=W0612
import random
from CardEffectsLogic import activateCard, isCoinCard, useBuyPhaseEffect

class Player:
    name=''
    actions=1
    buys=1
    coins=0
    deck=[]
    hand=[]
    discard=[]
    usedCards=[]
    buyPhaseEffects = []


    def newTurn(self):
        self.actions=1
        self.buys=1
        self.coins=0
        for c in self.usedCards:
            self.discard.append(c)
        self.usedCards = []     
        self.buyPhaseEffects = []   
        self.newHand()

    def __init__(self, name):
        self.name=name
        self.actions=1
        self.buys=1
        self.coins=0
        self.deck =['Estate','Estate','Estate','Copper','Copper','Copper','Copper','Copper','Copper','Copper']
        self.newHand()

    #json version of the object
    def out(self):
        resp = f'''{'{'}"name":"{self.name}","actions":"{self.actions}","buys":"{self.buys}","coins":"{self.coins}", "hand":['''
        for c in self.hand:
            resp = resp + '''"''' + c + '''",'''
        resp = resp.rstrip(',')
        resp = resp + ']}'

        return resp

    def newHand(self):
        #add a card here to test
        self.hand.append("Smithy")
        for i in range(0,5):
            self.drawCard()


    def drawCard(self):
        if len(self.deck) == 0:
            if len(self.discard) == 0:
                return
            for c in self.discard:
                self.deck.append(c)
            self.discard =[]
            random.shuffle(self.deck)
        cardIndex = random.choice(range(0, len(self.deck)))
        self.hand.append(self.deck[cardIndex])
        del self.deck[cardIndex]
        
    def gainCard(self, cardName):
        self.discard.append(cardName)

    #need a different method for attacks
    def tryUseCardAsAction(self, cardName):
        if cardName not in self.hand:
            return False
        if self.actions > 0:
            actionResult = activateCard(cardName, self)
            if actionResult == True:
                self.actions = self.actions - 1
                self.hand.remove(cardName)
                self.usedCards.append(cardName)
                return True
        return False
    
    def tryUseCoinCard(self, cardName):
        if cardName not in self.hand:
            return False
        actionResult = activateCard(cardName, self)
        self.hand.remove(cardName)
        self.usedCards.append(cardName)
        return True
    
    def calculateCoins(self):
        for c in self.hand:
            if not isCoinCard(c) :
                self.usedCards.append(c)
                self.hand.remove(c)
        for effect in self.buyPhaseEffects:
            useBuyPhaseEffect(effect, self)
        for cc in self.hand :
            activateCard(cc, self)

    def AddCardToDeck(self, cardName):
        self.deck.append(cardName)

    def AddCardToHand(self, cardName):
        self.hand.append(cardName)

    def AddCardToDiscard(self, cardName):
        self.discard.append(cardName)
        
    def AddBuyPhaseEffect(self, cardName):
        self.buyPhaseEffects.append(cardName)
    
    def IncreaseActions(self, num):
        self.actions = self.actions + num

    def IncreaseBuys(self, num):
        self.buys = self.buys + num

    def IncreaseCoins(self, num):
        self.coins = self.coins + num

    def DrawCards(self, num):
        for i in range(0, int(num)):
            self.drawCard()