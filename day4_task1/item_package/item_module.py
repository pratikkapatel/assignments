class Item:

    def __int__(self):
        id = None
        desc = None
        quantity = None
        price = None

    def calc_final_price(self):
        if self.quantity == 2:
            total = self.quantity * self.price
            final_price = (total - (total*(10/100)))
            print(final_price)
        elif 5 >= self.quantity >= 3:
            total = self.quantity * self.price
            final_price = (total - (total*(15/100)))
            print(final_price)
        elif self.quantity > 5:
            total = self.quantity * self.price
            final_price = (total - (total * (25 / 100)))
            print(final_price)
        else:
            print("No discount, enter valid quantity")
