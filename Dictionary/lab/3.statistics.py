products = {}
# total_products = 0
# total_quantity = 0
while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    product = command[0]
    quantity = command[1]
    if product not in products.keys():
        products[product] = 0
    products[product] += int(quantity)

print("Products in stock:")
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")


