# -*- coding: utf-8 -*-
from .cage import Cage
from .player import Player


class Bingo(object):
    """
    attributes
        players: expected as list, which contains string elements
        cage: Cage class
    """
    def __init__(self, players):
        self.players = {p: Player(p) for p in players}
        self.cage = Cage()
        self.current_number = 0

    def draw(self):
        self.current_number = self.cage.pop()
        for x in self.players:
            self.players[x].punch(self.current_number)

        return self.current_number

    @property
    def winners(self):
        return [x for x in self.players if self.players[x].is_bingo()]
