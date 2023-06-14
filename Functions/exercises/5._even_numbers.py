
number = input().split(" ")
mylist = []

for num in number:
    mylist.append(int(num))
filtered_list = filter(lambda x: (x % 2 == 0), mylist)
even_number = list(filtered_list)
print(even_number)