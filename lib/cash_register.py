class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes a new CashRegister instance.
        
        Args:
            discount (int): Discount percentage (default is 0).
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0  # To track the last transaction for voiding

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the cash register.
        
        Args:
            title (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item (default is 1).
        """
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity  # Store the last transaction value

    def apply_discount(self):
        """
        Applies a discount to the total and prints the correct message.
        """
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Convert total to an integer if it has no decimal part
            if self.total == int(self.total):
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        """
        Returns the list of items in the cash register.
        """
        return self.items

    def void_last_transaction(self):
        """
        Removes the last transaction from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset last transaction to avoid accidental voiding again
