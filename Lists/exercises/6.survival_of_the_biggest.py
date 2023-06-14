word = input().split()
numbers_to_remove = int(input())

my_letters_list = []

for ch in word:
    my_letters_list.append(int(ch))
for iterations in range(numbers_to_remove):
    my_letters_list.remove(min(my_letters_list))
print(', '.join(map(str, my_letters_list)))


