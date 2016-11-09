# -*- coding: utf-8 -*-
from cage import Cage
from player import Player


class Bingo(object):
    """
    attributes
        players: expected as list, which contains string elements
        cage: Cage class
    """
    def __init__(self, players):
        self.users = {p: Player(p) for p in players}
        self.cage = Cage()

    def draw(self):
        return self.cage.pop()

    def winners(self):
        return [p for p in self.players if p.card_check]
