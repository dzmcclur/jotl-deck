import unittest
from deck import Deck

class TestDeckMethods(unittest.TestCase):

    def test_set_base_deck(self):
        test_deck = Deck()
        card_list = [1,2,3]
        test_deck.set_base_deck(card_list)
        self.assertListEqual(test_deck.base_cards,card_list)

    def test_add_cards(self):
        test_deck = Deck()
        card_list = [4,5,6]
        test_deck.add_cards(*card_list)
        self.assertListEqual(test_deck.added_cards,card_list)

    def test_add_cards_with_shuffle(self):
        test_deck = Deck()
        card_list = [4,5,6]
        test_deck.add_cards(*card_list,reshuffle=True)
        self.assertCountEqual(test_deck.draw_pile,card_list)

    def test_draw_card(self):
        test_deck = Deck()
        card_list = [1,2,3]
        test_deck.base_cards = card_list[:]
        test_deck.draw_pile = card_list[:]

        card = test_deck.draw_card()
        
        self.assertIn(card,test_deck.base_cards)
        self.assertNotIn(card,test_deck.draw_pile)

    def test_shuffle_deck(self):
        test_deck = Deck()
        card_list = [1,2,3]
        test_deck.base_cards = card_list[:]
        test_deck.draw_pile = card_list[0:2]

        test_deck.shuffle_deck()

        self.assertCountEqual(test_deck.draw_pile, test_deck.base_cards[0:2])

    def test_reshuffle_deck(self):
        test_deck = Deck()
        card_list1 = [1,2,3]
        card_list2 = [4,5,6]
        test_deck.base_cards = card_list1[:]
        test_deck.added_cards = card_list2[:]
        test_deck.draw_pile = card_list1[0:2] + card_list2[0:2]
        test_deck.discard_pile = [ card_list1[2], card_list2[2] ]

        test_deck.reshuffle_deck()

        self.assertCountEqual(test_deck.draw_pile, test_deck.base_cards + test_deck.added_cards)
        self.assertListEqual(test_deck.discard_pile, [])

    def test_reset_deck(self):
        test_deck = Deck()
        card_list1 = [1,2,3]
        card_list2 = [4,5,6]
        test_deck.base_cards = card_list1[:]
        test_deck.added_cards = card_list2[:]

        test_deck.reset_deck()

        self.assertCountEqual(test_deck.base_cards, card_list1)
        self.assertListEqual(test_deck.added_cards, [])

if __name__ == '__main__':
    unittest.main()