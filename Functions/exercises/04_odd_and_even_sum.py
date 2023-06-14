def totals(number):
    total_even = 0
    total_odd = 0
    for num in number:
        if int(num) % 2 == 0:
            total_even += int(num)
        else:
            total_odd += int(num)
    return total_even, total_odd


number_input = input()
total_even, total_odd = totals(number_input)
print(f"Odd sum = {total_odd}, Even sum = {total_even}")