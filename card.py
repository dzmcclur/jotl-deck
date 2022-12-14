class LazyProperty(object):

    def __get__(self, obj, objtype=None):
        pass

class Card:

    image = LazyProperty()

    def __init__(self, id=0, name='Unnamed Card', path='', rollover = False, shuffle_after = False, remove_after = False):
        self.card_id = id
        self.name = name
        self.image_path = path
        self.rollover = rollover
        self.shuffle_after = shuffle_after
        self.remove_after = remove_after

    # def get_attributes(self):
        """Returns values for name, image, rollover, shuffle_after, and remove_after in dict format"""