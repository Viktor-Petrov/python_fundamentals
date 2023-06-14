single_string = input().split(", ")
beggars_count = int(input())

single_string_as_digit = []
for element in single_string:
    single_string_as_digit.append(int(element))

total_beggar_money = []
current_index = 0
while current_index < beggars_count:
    current_beggar_money = 0
    for current_sum in range(current_index, len(single_string_as_digit), beggars_count):
        current_beggar_money += single_string_as_digit[current_sum]
    total_beggar_money.append(current_beggar_money)
    current_index += 1
print(total_beggar_money)









#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# money_received = input().split(", ")
# number_of_beggars = int(input())
#
# money_received_as_int = []
# for digit in money_received:
#     money_received_as_int.append(int(digit))
#
# current_index = 0
# total_beggar_money = []
# while current_index < number_of_beggars:
#     current_beggars_money = 0
#     for current_sum in range(current_index, len(money_received_as_int), number_of_beggars):
#         current_beggars_money += money_received_as_int[current_sum]
#     total_beggar_money.append(current_beggars_money)
#     current_index += 1
# print(total_beggar_money)
#
#
