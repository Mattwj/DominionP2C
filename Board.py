# -*- coding: utf-8 -*-
from Player import Player

class Board:
    players = []

    def __init__(self):
        self.players= []

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