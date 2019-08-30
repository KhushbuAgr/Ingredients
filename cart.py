from decimal import getcontext,Decimal

class Cart:

    shopping_cart = []

    #constructor of cart which takes ingredientStore class instance as input
    def __init__(self,ingredientStoreInstance):
         self.ingredient_store_instance = ingredientStoreInstance

    #add items in the shopping cart, default value of quantity is 1
    def add(self,item,qty=1):
         print("item inside cart ", item)
         Cart.shopping_cart.append([item,qty])

    # perform total value for the cart based on the item,quantity and discount
    def get_total(self,discounts=None):
        total_cost  = Decimal(0)
        getcontext().prec = 3
        if discounts is not None:
            for product,quantity in Cart.shopping_cart:
                print("product inside get total ", product)
                print("quantity inside get total ", quantity)
                for discount_instance in discounts:
                     if (product in discount_instance.get_item() ):
                        print("discount_instance.get_quantity()", discount_instance.get_quantity())
                        buy_quantity = discount_instance.calculate_line_total(quantity);
                        print("buy_quantity", buy_quantity)
                total_cost += Decimal(buy_quantity) * (self.ingredient_store_instance.get_ingredient_price(product))
                print("total_cost: ",total_cost)
                print("ingredient_store_instance.get_ingredient_price(product) ", self.ingredient_store_instance.get_ingredient_price(product))
            return total_cost
        else:
            for product,quantity in Cart.shopping_cart:
                total_cost += Decimal(quantity) * (self.ingredient_store_instance.get_ingredient_price(product))
            return total_cost



