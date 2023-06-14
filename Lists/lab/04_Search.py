number_of_lines = int(input())
word = input()
my_list = []
removed_list = []

for ch in range(number_of_lines):
    current_string = input()
    my_list.append(current_string)
    if word in current_string:
        removed_list.append(current_string)

print(my_list)
print(removed_list)
