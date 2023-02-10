# -*- coding: utf-8 -*-
from Player import Player
from random import choice, shuffle

class Board:
    players = []
    cards = {}
    gamestarted = False
    usableCards = []
    playerOrder = []
    
    def __init__(self):
        self.players = []
        self.cards = {}
        self.gamestarted = False
        self.playerOrder = []
        self.usableCards = ["Smithy","Village","Market", "Moat", "Festival", "Laboratory", "Merchant", "Witch", "Council Room", "Harem"]

    def fullReset(self):
        self.players = []
        self.cards = {}
        self.gamestarted = False
        self.playerOrder = []
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
        if gamestarted == True:
            return False
        
        if len(self.players) > 0 :
            gamestarted = True
        else :
            return False
        
        shuffled = shuffle(self.players)
        
        for p in shuffled :
            self.playerOrder.push(p.name)
        
        if len(self.players) == 2 :
            self.cards["Estate"] = 8
            self.cards["Duchy"] = 8
            self.cards["Province"] = 8
            self.cards["Curse"] = 10
            self.cards["Gold"] = -1
            self.cards["Silver"] = -1
            self.cards["Copper"] = -1
            
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
            self.cards.push(card)
            self.usableCards.remove(card)        
    
    def passTurn(self, player):
        player.newTurn()
        if self.playerOrder[-1] == player.name:
            return self.getPlayer(self.playerOrder[0])
        else :
            nextIsGood = False
            for name in self.playerOrder:
                if nextIsGood == True :
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