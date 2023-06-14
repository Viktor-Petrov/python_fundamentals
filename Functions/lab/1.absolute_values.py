numbers = input().split(' ')

abs_list = []

for element in numbers:
    abs_list.append(abs(float(element)))
print(abs_list)
