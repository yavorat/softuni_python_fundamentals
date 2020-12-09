product_data = input()

products = {}

while not product_data == "statistics":
    product, quantity = product_data.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

    product_data = input()