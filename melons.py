class Melon(object):

    """This file should have our melon-type classes in it."""

    def __init__(self, melon_type, origin, shape, diff_to_grow, season):
        """ diff_to_grow should be True or False"""

        self.melon_type = melon_type.lower()
        self.origin = origin.lower()
        self.shape = shape.lower()
        self.diff_to_grow = diff_to_grow
        self.season = season.lower()


    def price(self):
        price = 5
        if self.origin == "imported":
            price = price * 1.5 
        if self.shape == "square":
            price = price * 2
        if self.diff_to_grow == True:
            price = price + 1
        return float(price)
