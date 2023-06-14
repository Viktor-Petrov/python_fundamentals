factor = int(input())
count = int(input())
my_list = []

for num in range(1, count + 1):
    current_num = num * factor
    my_list.append(current_num)

print(my_list)

