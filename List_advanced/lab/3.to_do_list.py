mylist = []

while True:
    command = input()
    if command == "End":
        break

    split_command = command.split('-')
    position = int(split_command[0])
    name = split_command[1]
    mylist.append([position, name])

sorted_list = []
for word in sorted(mylist):
    sorted_list.append(word[1])
print(sorted_list)