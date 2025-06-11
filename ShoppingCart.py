class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty, price):
        # Add price to item tuple
        item = (item_name, qty, price)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]  # qty * price
        return total

    def cart_contents(self):
        print("Cart Contents: ")
        for name, qty, price in self.items:
            print(f"  {name}: {qty} x {price} = {qty * price}")
        print(f"Total Amount: {self.calculate_total():.2f}\n")

class DiscountedCart(ShoppingCart):
    def __init__(self,discount_rate: float):
        super().__init__()
        self.discount_rate = discount_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        return initial_total - discount

class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax

def checkout(cart: ShoppingCart):
    cart.cart_contents()
    print(f"Total amount after adjustments: {cart.calculate_total():.2f}\n")


    # 1) Ordinary Cart
obj_cart = ShoppingCart()
obj_cart.add_item("Papaya", 76, 6.20)
obj_cart.add_item("Orange", 96, 11.50)
obj_cart.add_item("Kiwi", 85, 9.60)
print(">>> Ordinary Cart Without Tax & Discount <<<")
checkout(obj_cart)

    # 2) Discounted Cart (15% Discount)
disc_cart = DiscountedCart( 0.15)
disc_cart.add_item("Papaya", 76, 6.20)
disc_cart.add_item("Orange", 96, 11.50)
disc_cart.add_item("Kiwi", 85, 9.60)
print(">>> Applying a 15% Discount <<<")
checkout(disc_cart)

    # 3) Taxed Cart (7% Tax)
taxed_cart = TaxedCart(tax_rate= 0.07)
taxed_cart.add_item("Papaya", 5, 2.00)
taxed_cart.add_item("Orange", 96, 11.50)
taxed_cart.add_item("Kiwi", 3, 1.50)
print(">>> Applying a 7% Tax  <<<")
checkout(taxed_cart)