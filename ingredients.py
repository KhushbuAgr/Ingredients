import os
import csv
from decimal import Decimal


class IngredientsStore:
    ingredients = []
    def __init__(self,input_ingredients):
        self.ingredients = input_ingredients

    # gives the price of a item supplied
    def get_ingredient_price(self, item):
        for ingredient in self.ingredients:
            if ingredient[0] == item:
                  return Decimal(ingredient[1])
