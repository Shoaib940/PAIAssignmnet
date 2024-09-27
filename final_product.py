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
  def get_price(self, quantity):
      try:
          if quantity <= 0:
              raise ValueError("Quantity must be greater than 0.")
          if 0 < quantity < 10:
            return self.price * quantity
          elif 10 <= quantity <= 99:
            return ((self.price * quantity) - (0.1 * (self.price * quantity)))
          elif quantity >= 100:
            return ((self.price * quantity) - (0.2 * (self.price * quantity)))
      except ValueError as e:
          print(f"Error")
          return None
        # Create product object
product = Product("Laptop", 150, 1000)

# Test cases
product.make_purchase(7)  
product.make_purchase(1) 
product.make_purchase(120) 
product.make_purchase(-05) 
product.make_purchase(3) 
