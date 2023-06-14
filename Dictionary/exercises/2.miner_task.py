mydict = {}

while True:
    command = input()
    if command == "stop":
        break
    resource = int(input())
    if command not in mydict.keys():
        mydict[command] = 0
    mydict[command] += resource

for command, resource in mydict.items():
    print(f"{command} -> {resource}")