class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      return None

  def make_purchase(self, quantity):
    try:
        if quantity > self.amount:
            raise ValueError("Not enough stocks")
        elif quantity < 0:
            raise ValueError("TInvalid number of items")
        print(f"Your order has been placed, Total: ${self.get_price(quantity)}")
        self.amount= self.amount-quantity
        
    except ValueError as e:
            print(f"Error")
        