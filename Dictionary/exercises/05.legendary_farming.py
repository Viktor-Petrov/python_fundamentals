materials = input().split()
mydict = {}
while True:
    for i in range(0, len(materials), 2):
        value = int(materials[i])
        key = materials[i + 1].lower()
        if key not in mydict.keys():
            mydict[key] = 0
        mydict[key] += value
        if mydict['shards'] >= 250:
            print("Shadowmourne obtained!")
            mydict["shards"] -= 250
            break
        elif mydict["fragments"] >= 250:
            print("Valanyr obtained!")
            mydict["fragments"] -= 250
            break
        elif mydict["motes"] >= 250:
            print("Dragonwrath obtained!")
            mydict["motes"] -= 250
            break
    break
for key, value in mydict.items():
    print(f"{key}: {value}")