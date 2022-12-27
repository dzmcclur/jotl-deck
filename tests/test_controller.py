import unittest
from deck import Deck
from controller import Controller

class TestDisplayMethods(unittest.TestCase):
    def setUp(self):
        self.test_controller = Controller() # new display
        # self.test_deck = Deck() # new deck

    def test_load_deck_from_file(self):
        card_list = [1,2,3]
        self.assertCountEqual([], self.test_controller.deck.base_cards) # check empty
        
        # load deck
        test_deck_id = 'test_deck_id1'
        filepath = test_deck_id + '.csv'
        with open(f'./tests/{filepath}','w') as test_saved_deck:
            for card in card_list:
                test_saved_deck.writelines(f'{card}\n')
        self.test_controller.load_deck(f'./tests/{filepath}')

        # check cards in deck
        self.assertEqual(self.test_controller.deck.deck_id, test_deck_id)
        self.assertCountEqual(card_list, self.test_controller.deck.base_cards)

    def test_save_deck_to_file(self):
        test_deck_id = 'test_deck_id2'
        test_deck = Deck(test_deck_id, 'Test Deck 2')
        test_deck.base_cards = [1,2,3]
        self.test_controller.deck = test_deck

        # save deck
        filepath = test_deck_id + '.csv'
        self.test_controller.save_deck(f'./tests/')

        # check file exists and data saved
        self.test_controller.deck = Deck()
        self.test_controller.load_deck(f'./tests/{filepath}')
        self.assertEqual(self.test_controller.deck.deck_id, test_deck_id)
        self.assertCountEqual(test_deck.base_cards, self.test_controller.deck.base_cards)
        pass

    def test_add_card_to_deck(self):
        # new deck
        # add card
        # deck includes card
        pass

    def test_draw_card(self):
        # new deck
        # draw card id
        # card values from id
        pass

    def test_card_image_not_found(self):
        # card
        # no image path
        # graceful recovery
        pass

    """
    Section below is commented for future implementation -

    def test_draw_rollover(self):
        # new deck
        # draw card id
        # card values from id
        # rollover true
        # draw again
        pass

    def test_draw_remove_after_only(self):
        # new deck
        # draw card id
        # card values from id
        # shuffle_after true
        # reshuffle_deck
        pass

    def test_draw_shuffle_after_only(self):
        # new deck
        # draw card id
        # card values from id
        # shuffle_after true
        # reshuffle_deck
        pass

    def test_draw_remove_and_shuffle_after(self):
        # new deck
        # draw card id
        # card values from id
        # shuffle_after true
        # reshuffle_deck
        pass
    """

    def test_reshuffle_deck(self):
        # deck
        # draw and discard
        # reshuffle
        # all cards back
        pass

    def test_reset_deck(self):
        # deck
        # add cards
        # reset
        # check deck reverted
        pass

if __name__ == '__main__':
    unittest.main()