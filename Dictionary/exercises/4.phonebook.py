
phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone

for i in range(int(entry)):
    searched_name = input()
    if searched_name not in phonebook.keys():
        print(f'Contact {searched_name} does not exist.')
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
