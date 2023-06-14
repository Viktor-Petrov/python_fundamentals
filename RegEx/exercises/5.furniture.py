import re

pattern = r">>([A-Z][A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"
total_cost = 0
all_furniture = []

while True:
    command = input()
    if command == "Purchase":
        break
    else:
        matches = re.findall(pattern, command)
        for match in matches:
            furniture, price, quantity = match[0], match[1], match[2]
            all_furniture.append(furniture)
            total_cost += float(price) * int(quantity)

print("Bought furniture:")
for furnitures in all_furniture:
    print(furnitures)
print(f"Total money spend: {total_cost:.2f}")