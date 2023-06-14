number_of_lines = int(input())
odd_list = []
even_list = []
negative_list = []
positive_list = []

for i in range(number_of_lines):
    current_int = int(input())

    if current_int % 2 == 0:
        even_list.append(current_int)
    if current_int % 2 != 0:
        odd_list.append(current_int)
    if current_int < 0:
        negative_list.append(current_int)
    if current_int >= 0:
       positive_list.append(current_int)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)





#
#
# number_of_lines = int(input())
#
# # constant values
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_POSITIVE = 'positive'
# COMMAND_NEGATIVE = 'negative'
#
# # accepting numbers from user input
# numbers = []
#
# for _ in range(number_of_lines):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
#
# filtered_numbers = []
#
# # number_filtering
# for number in numbers:
#     filtered_passes = (
#             (command == COMMAND_EVEN and number % 2 == 0) or
#             (command == COMMAND_ODD and number % 2 != 0) or
#             (command == COMMAND_NEGATIVE and number < 0) or
#             (command == COMMAND_POSITIVE and number >= 0)
#     )
#     if filtered_passes:
#         filtered_numbers.append(number)
#
# print(filtered_numbers)