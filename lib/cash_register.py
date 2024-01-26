#!/usr/bin/env python3
 
class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.last_transactions.append({'item': item, 'price': price, 'quantity': quantity})

    def apply_discount(self):
        if self.discount > 0:
          self.total -= int(self.total * (self.discount / 100))
          print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")


    def void_last_transaction(self):
      if not self.last_transactions:
        return "There is no transaction to void."
      amount_to_subtract = self.last_transactions[-1]['price'] * self.last_transactions[-1]['quantity']
      self.total -= amount_to_subtract
      self.last_transactions.clear()
      
  

cash_register = CashRegister(10)
cash_register.add_item('milk', 2.50)
cash_register.add_item('milk', 2.50)
cash_register.add_item('salt', 2.30)
cash_register.add_item('scones', 5.45)

print(cash_register.last_transactions)
cash_register.void_last_transaction()
print(cash_register.last_transactions)