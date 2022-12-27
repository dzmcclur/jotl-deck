import unittest
from deck import Deck

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()
        self.card_list1 = [1,2,3]
        self.card_list2 = [4,5,6,7]

    def test_set_base_deck(self):
        self.test_deck.set_base_deck(self.card_list1)
        self.assertListEqual(self.test_deck.base_cards, self.card_list1)

    def test_add_cards(self):
        self.test_deck.add_cards(*self.card_list2)
        self.assertListEqual(self.test_deck.added_cards, self.card_list2)

    def test_add_cards_with_shuffle(self):
        self.test_deck.add_cards(*self.card_list2, reshuffle=True)
        self.assertCountEqual(self.test_deck.draw_pile, self.card_list2)

    def test_draw_card(self):
        self.test_deck.base_cards = self.card_list1[:]
        self.test_deck.draw_pile = self.card_list1[:]

        card = self.test_deck.draw_card()
        
        self.assertIn(card, self.test_deck.base_cards)
        self.assertNotIn(card, self.test_deck.draw_pile)

    def test_shuffle_deck(self):
        self.test_deck.base_cards = self.card_list1[:]
        self.test_deck.draw_pile = self.card_list1[0:2]

        self.test_deck.shuffle_deck()

        self.assertCountEqual(self.test_deck.draw_pile, self.test_deck.base_cards[0:2])

    def test_reshuffle_deck(self):
        self.test_deck.base_cards = self.card_list1[:]
        self.test_deck.added_cards = self.card_list2[:]
        self.test_deck.draw_pile = self.card_list1[0:2] + self.card_list2[0:2]
        self.test_deck.discard_pile = [ self.card_list1[2], self.card_list2[2] ]

        self.test_deck.reshuffle_deck()

        self.assertCountEqual(self.test_deck.draw_pile, self.test_deck.base_cards + self.test_deck.added_cards)
        self.assertListEqual(self.test_deck.discard_pile, [])

    def test_reset_deck(self):
        self.test_deck.base_cards = self.card_list1[:]
        self.test_deck.added_cards = self.card_list2[:]

        self.test_deck.reset_deck()

        self.assertCountEqual(self.test_deck.base_cards, self.card_list1)
        self.assertListEqual(self.test_deck.added_cards, [])

if __name__ == '__main__':
    unittest.main()