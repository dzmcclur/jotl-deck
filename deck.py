import random
from typing import Dict, List, Tuple
from validator import Validator

class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')

class Deck:

    deck_type = OneOf('monster', 'player')

    def __init__(self, deck_id=0, name='Unnamed Deck', deck_type='monster'):
        self.deck_id = deck_id
        self.name = name
        self.base_cards = []
        self.added_cards = []
        self.draw_pile = []
        self.discard_pile = []
        self.deck_type = deck_type

    def __str__(self):
        return f'{self.name} is a {self.deck_type} deck with {len(self.base_cards)} cards'

    def set_base_deck(self, card_list: List[int]) -> None:
        """Stores input integers as "base" deck.

        Keyword arguments:
        card_list -- list of int values
        """
        self.base_cards = card_list[:]

    def add_cards(self, *args, reshuffle=False):
        """Stores input integers as additional, temporary cards in the deck. Can reshuffle with optional "reshuffle" flag.

        Keyword arguments:
        card_list -- list of int values
        """
        self.added_cards = list(args)
        if reshuffle:
            self.reshuffle_deck()

    def draw_card(self):
        """Return value of first card in deck, which is added to discard pile."""
        drawn_card = self.draw_pile.pop(0)
        self.discard_pile.append(drawn_card)
        return drawn_card

    def shuffle_deck(self):
        """Randomizes the order of remaining cards in the deck, without changing discarded cards."""
        new_draw_pile = []
        for i in range(len(self.draw_pile)):
            chosen_card = random.choice(self.draw_pile)
            new_draw_pile.append(chosen_card)
            self.draw_pile.remove(chosen_card)
        self.draw_pile = new_draw_pile[:]

    def reshuffle_deck(self):
        """Empties the discard pile and shuffles (shuffle_deck) a new deck of base + additional cards"""
        self.discard_pile = []
        self.draw_pile = self.base_cards + self.added_cards
        self.shuffle_deck()

    def reset_deck(self):
        """Empties all additional cards from deck, then reshuffle (reshuffle_deck)"""
        self.added_cards = []
        self.reshuffle_deck()
