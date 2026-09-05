#!/usr/bin/env python3

# Coffee represents a coffee carried by the bookstore.

class Coffee:
    def __init__(self, size, price):

# size goes through the property setter.

      self.size = size
      self.price = price

# Return the current size.
    @property
    def size(self):
       return self._size

    @size.setter
    def size(self, size):
       if size not in ("Small", "Medium", "Large"):
          print("size must be Small, Medium, or Large")
       else:
          self._size = size

    # Leave a tip for the coffee, increasing its price by 1.
    def tip(self):
       print("This coffee is great, here’s a tip!")
       self.price += 1