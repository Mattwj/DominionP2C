# -*- coding: utf-8 -*-
from CardEffectsLogic import isVictoryCard
from Player import Player
from random import choice, shuffle

class Board:
    players = []
    cards = {}
    gamestarted = False
    usableCards = []
    playerOrder = []
    usedCards = []
    currPlayer = ""
    
    def __init__(self):
        self.players = []
        self.cards = {}
        self.gamestarted = False
        self.playerOrder = []
        self.usedCards = []
        self.currPlayer = ""
        self.usableCards = ["Smithy","Village","Market", "Moat", "Festival", "Laboratory", "Merchant", "Witch", "Council Room", "Harem"]

    def fullReset(self):
        self.players.clear()
        self.cards.clear()
        self.usedCards.clear()
        self.gamestarted = False
        self.playerOrder.clear()
        self.currPlayer = ""
        self.usableCards = ["Smithy","Village","Market", "Moat", "Festival", "Laboratory", "Merchant", "Witch", "Council Room", "Harem"]
        

    def addPlayer(self, name):
        found = False
        for p in self.players:
            if p.name == name:
                found = True
        if found == False:
            self.players.append(Player(name))
            return "true"
        return "false"

    def getPlayer(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None
    
    def startGame(self):
        if self.gamestarted == True:
            return False
        
        if len(self.players) > 1 :
            self.gamestarted = True
        else :
            return False
        
        shuffled = self.players
        
        shuffle(shuffled)
        
        for p in shuffled :
            self.playerOrder.append(p.name)
        
        self.currPlayer = self.playerOrder[0]
        
        self.pickFromUsableCards()
        
        if len(self.players) == 2 :
            self.cards["Estate"] = 8
            self.cards["Duchy"] = 8
            self.cards["Province"] = 8
            self.cards["Curse"] = 10
            self.cards["Gold"] = -1
            self.cards["Silver"] = -1
            self.cards["Copper"] = -1
            for card in self.usedCards:
                if isVictoryCard(card):
                    self.cards[card] = 8
                else :
                    self.cards[card] = 10
        return True
            
    def performPotentialAttackOnOthers(self, player, cardName) :
        if cardName == "Witch" :
            if self.cards["Curse"] > 0:
                for p in self.players:
                    if self.cards["Curse"] > 0:
                        if p.name != player.name :
                            if "Moat" not in p.hand :
                                p.gainCard("Curse")
                                self.cards["Curse"] = self.cards["Curse"] - 1
                                
    def performPotentialEffectOnOthers(self, player, cardName) :
        if cardName == "Council Room" :
            for p in self.players:
                if p != player.name:
                    p.DrawCards(1)
    
    def pickFromUsableCards(self):
        for i in range(10):
            card = choice(self.usableCards)
            self.usedCards.append(card)
            self.usableCards.remove(card)        
    
    def passTurn(self, player):
        player.newTurn()
        if self.playerOrder[-1] == player.name:
            self.currPlayer = self.playerOrder[0]
            return self.getPlayer(self.playerOrder[0])
        else :
            nextIsGood = False
            for name in self.playerOrder:
                if nextIsGood == True :
                    self.currPlayer = name
                    return self.getPlayer(name)  
                if name == player.name:
                    nextIsGood = True
    
    def getCards(self):
        resp = '''"cards":['''
        for c in self.cards:
            resp = resp + '''"''' + c + '''",'''
        resp = resp.rstrip(',')
        resp = resp + ']}'
        return resp