number_of_lines = int(input())
positive_counter = 0
positive_list = []
negative_list = []

for num in range(number_of_lines):
    current_number = int(input())
    if current_number < 0:
        negative_list.append(current_number)
    else:
        positive_list.append(current_number)
        positive_counter += 1
print(positive_list)
print(negative_list)
print(f'Count of positives: {positive_counter}')
negative_sum = sum(negative_list)
print(f'Sum of negatives: {negative_sum}')
