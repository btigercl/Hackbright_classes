class Melon(object):

    """This file should have our melon-type classes in it."""

    def __init__(self, melon_type, origin, shape, diff_to_grow, season):
        """ diff_to_grow should be True or False"""

        self.melon_type = melon_type.lower()
        self.origin = origin.lower()
        self.shape = shape.lower()
        self.diff_to_grow = diff_to_grow
        self.season = season.lower()


    def price(self, quantity):

        price = 5.00
        if self.origin == "imported":
            price = price * 1.5 
        if self.shape == "square":
            price = price * 2
        if self.diff_to_grow == True:
            price = price + 1
        price = price * quantity
        if self.melon_type == "watermelon" and quantity >= 3:
            price = price * .75 
        if self.melon_type == "cantaloupe" and quantity >= 5:
            price = price * .50
        return price
