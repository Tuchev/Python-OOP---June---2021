class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        product_to_find = [product for product in self.products if product.name == product_name]
        if product_to_find:
            return product_to_find[0]

    def remove(self, product_name):
        product_to_find = [product for product in self.products if product.name == product_name]
        if product_to_find:
            self.products.remove(product_to_find[0])

    def __repr__(self):
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])