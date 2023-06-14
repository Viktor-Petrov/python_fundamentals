def calculation(product_type, number):
    if product_type == "coffee":
        price = 1.5
    if product_type == "water":
        price = 1.0
    if product_type == "coke":
        price = 1.4
    if product_type == "snacks":
        price = 2
    result = round(price * number, 2)
    return "{:.2f}".format(result)

product = input()
quantity = int(input())
print(calculation(product, quantity))

