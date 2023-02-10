# -*- coding: utf-8 -*-
from Player import Player
from random import choice

class Board:
    players = []
    cards = {}
    gamestarted = False
    usableCards = []
    
    def __init__(self):
        self.players= []
        usableCards = ["Smithy","Village","Market", "Moat", "Festival", "Laboratory", "Merchant", "Witch"]

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
        if len(self.players) == 2 :
            self.cards["Estate"] = 8
            self.cards["Duchy"] = 8
            self.cards["Province"] = 8
            self.cards["Curse"] = 10
            self.cards["Gold"] = -1
            self.cards["Silver"] = -1
            self.cards["Copper"] = -1
            
    def performAttackOnOthers(self, player, cardName) :
        if cardName == "Witch" :
            if self.cards["Curse"] > 0:
                for p in self.players:
                    if self.cards["Curse"] > 0:
                        if p.name != player.name :
                            if "Moat" not in p.hand :
                                p.gainCard("Curse")
                                self.cards["Curse"] = self.cards["Curse"] - 1
    
    def pickFromUsableCards(self):
        for i in range(10):
            card = choice(self.usableCards)
            self.cards.push(card)
            self.usableCards.remove(card)