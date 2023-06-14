single_string = input().split()
reverse_list = []

for element in single_string:
    current_element = -int(element)
    reverse_list.append(current_element)
print(reverse_list)