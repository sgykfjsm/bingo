# -*- coding: utf-8 -*-
from card import Card


class Player(object):
    def __init__(self, player_id):
        self.id = player_id
        self.card = Card()

    def punch(self, number):
        self.card.punch(number)

    def card_check(self):
        return self.card_is_bingo
