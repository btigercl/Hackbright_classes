class Melon(object):

    """This file should have our melon-type classes in it."""

    # def __init__(self, melon_type, origin, shape, diff_to_grow, season):
    #     """ diff_to_grow should be True or False"""

    #     self.melon_type = melon_type.lower()
    #     self.origin = origin.lower()
    #     self.shape = shape.lower()
    #     self.diff_to_grow = diff_to_grow
    #     self.seasons = season.lower()


    def price(self, qty):

        price = 5.00
        if self.imported == True:
            price = price * 1.5 
        if self.shape == 'square':
            price = price * 2
        price = price * qty

        return price

class Watermelon (Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def price(self, qty):

        base = super(Watermelon, self).price(qty) 
        if qty >= 3:
            price = base * .75 
        else:
            price = base
        return price

class Cantaloupe(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def price(self, qty):

        base = super(Cantaloupe, self).price(qty)
        if qty >= 5:
            price = base * .50
        else:
            price = base 
        return price

class Casaba(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def price(self, qty):

        base = super(Casaba, self).price(qty)   
        price = base + 1 

        return price