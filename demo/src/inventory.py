
class Product:
    
    def __init__(self, product_id, name, price, quantity=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price
    
    def restock(self, amount):
        if amount < 0:
            raise ValueError("Restock amount cannot be negative")
        self.quantity += amount
    
    def sell(self, amount):
        if amount < 0:
            raise ValueError("Sell amount cannot be negative")
        if amount > self.quantity:
            raise ValueError("Not enough inventory")
        self.quantity -= amount
        return amount * self.price


class Inventory:
    
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
    
    def get_product(self, product_id):
        if product_id not in self.products:
            return None
        return self.products[product_id]
    
    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def list_products(self):
        return list(self.products.values())
    
    def total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products.values())
