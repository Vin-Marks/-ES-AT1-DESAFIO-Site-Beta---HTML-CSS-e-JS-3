class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def display_cart(self):
        if not self.items:
            return "Seu carrinho está vazio."
        else:
            cart_content = "Seu carrinho contém:\n"
            for item in self.items:
                cart_content += f"Produto: {item.name} | Preço: R${item.price}\n"
            return cart_content

    def confirm_purchase(self):
        confirmation = input("Deseja confirmar a compra? (Sim/Não): ")
        if confirmation.lower() == "sim":
            return "Compra confirmada! Obrigado por comprar conosco."
        else:
            return "Compra não confirmada."


# Criando instâncias de produtos
product1 = Product(1, "Produto 1", "Descrição do produto 1", 100.00)
product2 = Product(2, "Produto 2", "Descrição do produto 2", 150.00)
product3 = Product(3, "Produto 3", "Descrição do produto 3", 200.00)

# Criando uma instância do carrinho de compras e adicionando produtos
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Exibindo o conteúdo do carrinho
print(cart.display_cart())

# Chamando a função de confirmação de compra
print(cart.confirm_purchase())
