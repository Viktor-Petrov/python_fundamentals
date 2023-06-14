wagons = int(input())
mylist = [0]*wagons

while True:
    command = input()
    if command == "End":
        break

    split_command = command.split(" ")
    current_command = split_command[0]

    if current_command == "add":
        add_people = int(split_command[1])
        mylist[-1] += add_people
    elif current_command == "insert":
        index = int(split_command[1])
        insert_people = int(split_command[2])
        mylist[index] += insert_people
    elif current_command == "leave":
        index = int(split_command[1])
        leave_people = int(split_command[2])
        mylist[index] -= leave_people

print(mylist)