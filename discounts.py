from abc import ABC, abstractmethod

#Abstract class which takes Item as mandatory field and buy_qty and free_qty as optional field
class AbstractDiscount(ABC):
    def __init__(self,item,buy_qty = 1,free_qty = None):
        self.item = item
        self.buy_qty = buy_qty
        self.free_qty = free_qty
        super(AbstractDiscount, self).__init__()

    # An abstract method which is just defined in this main class
    @abstractmethod
    def calculate_line_total(self,bought_qty):
        pass

#NoDiscount class will not have any discount hence just return the bought_qty as chargeble qty
class NoDiscount(AbstractDiscount):
    def calculate_line_total(self,bought_qty):
      return bought_qty

    def get_item(self):
        return self.item

    def get_quantity(self):
        return self.buy_qty

#BulkDiscount is the class, which return the chargeable qty based on the discount type
class BulkDiscount(AbstractDiscount):
    def calculate_line_total(self,bought_qty):
        print("bought_qty" ,bought_qty)
        print("buy_qty" ,self.buy_qty)
        print("free_qty" ,self.free_qty)
        if bought_qty > self.buy_qty:
          if (bought_qty%(self.buy_qty+self.free_qty) == 0):
              return (bought_qty//(self.buy_qty+self.free_qty)+ (bought_qty%self.buy_qty))
          else:
              return  ((bought_qty//self.buy_qty) + (bought_qty%(self.buy_qty+self.free_qty)))
        else:
            return bought_qty

    def get_item(self):
        return self.item

    def get_quantity(self):
        return self.buy_qty