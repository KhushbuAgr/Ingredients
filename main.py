from ingredients import *
from discounts import *
from cart import *
from decimal import Decimal


custom_ingredients = [
    ('chicken', Decimal('3.49')),
    ('tomatoes', Decimal('0.45')),
    ('onions', Decimal('2.00')),
    ('rice', Decimal('0.70')),
]

ingredient_store = IngredientsStore(custom_ingredients)

shopping_cart = Cart(ingredient_store)
#
shopping_cart.add('tomatoes')
shopping_cart.add('chicken')
shopping_cart.add('rice')
shopping_cart.add('onions',3)



tomatoes_nodiscount = NoDiscount('tomatoes')

# buy one get one free on tomatoes
buy_one_get_one_free_tomatoes = BulkDiscount('tomatoes', 1, 1)

# buy two get third free on onions
buy_two_get_third_free_onions = BulkDiscount('onions', 2, 1)

discounts=[buy_one_get_one_free_tomatoes, buy_two_get_third_free_onions,tomatoes_nodiscount]

total_after_discount = shopping_cart.get_total(discounts)


print("total_after_discount: " , total_after_discount)
