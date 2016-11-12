# -*- coding: utf-8 -*-
from .card import Card


class Player(object):
    def __init__(self, player_id, numbers=None):
        self.id = player_id
        self.card = Card(numbers)

    def punch(self, number):
        self.card.punch(number)

    def is_bingo(self):
        return self.card.is_bingo()
