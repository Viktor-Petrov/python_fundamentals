order_dict = {}

while True:
    orders = input().split(" ")
    if orders[0] == "buy":
        break
    name, price, quantity = orders[0], orders[1], orders[2]
    if name not in order_dict.keys():
        order_dict[name] = []
        if price not in order_dict.values():
            order_dict[name].append(price)
        else:
            new_price = price
            order_dict[name].replace(price, new_price)
    order_dict[name].append(quantity)
print(order_dict)
# for current_product in order_dict.items():
#     print(current_product)
