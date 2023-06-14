menu = input().split()
bakery = {}

for i in range(0, len(menu), 2):
    key = menu[i]
    value = menu[i + 1]
    bakery[key] = int(value)
print(bakery)

