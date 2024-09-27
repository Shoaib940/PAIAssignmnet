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