import unittest
from card import Card

class TestCardMethods(unittest.TestCase):

    def test_get_card_image_from_path(self):
        test_card_1 = Card()
        image_path = './tests/test_image.png'

        test_card_1.image_path = image_path

        self.assertIsNotNone(test_card_1.image)

    def test_get_card_image_error(self):
        test_card_1 = Card()
        image_path = 'bad path'
        error_message = f'[Errno 2] No such file or directory: \'{image_path}\''
        test_card_1.image_path = image_path

        self.assertRaisesRegex(RuntimeError, error_message, test_card_1.image)

if __name__ == '__main__':
    unittest.main()