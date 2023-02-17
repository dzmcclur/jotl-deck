from PIL import Image

class LazyProperty(object):

    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class Card:

    @LazyProperty
    def image(self):
        try:
            with Image.open(self.image_path, mode='r') as image_blob:
                return image_blob
        except IOError as e:
            print(e)
            pass
        return None

    def __init__(self, id=0, name='Unnamed Card', path='nopath', rollover=False, shuffle_after=False, remove_after=False):
        self.card_id = id
        self.name = name
        self.image_path = path
        self.rollover = rollover
        self.shuffle_after = shuffle_after
        self.remove_after = remove_after
