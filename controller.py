from deck import Deck

class Controller:
    def __init__(self):
        self.deck = Deck()
        pass

    def load_deck(self, filepath: str) -> None:
        self.deck.deck_id = filepath.split('/')[-1].split('.csv')[0]
        card_list = []

        with open(filepath, mode = 'r') as file:
            for line in file:
                card_list.append(int(line.strip()))
        file.close()
        
        self.deck.base_cards = card_list[:]

    def save_deck(self, filepath: str='') -> None:
        if (self.deck.deck_id == 0):
            print('Save Failed: Deck does not have an ID')
            return
        with open(f'{filepath}/{self.deck.deck_id}.csv','w') as saved_deck:
            for card in self.deck.base_cards + self.deck.added_cards:
                saved_deck.writelines(f'{card}\n')
        return