def ch_in_between(first, second):
    mylist = []
    for ch in range(ord(first) + 1, ord(second)):
        mylist.append(chr(ch))
    return mylist


first_character = input()
second_character = input()
print(' '.join(ch_in_between(first_character, second_character)))


