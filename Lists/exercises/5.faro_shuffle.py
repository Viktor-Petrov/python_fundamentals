cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    shuffle_cards = []
    middle = len(cards) // 2
    left = cards[0:middle]
    right = cards[middle::]
    for current_index in range(len(left)):
        shuffle_cards.append(left[current_index])
        shuffle_cards.append(right[current_index])
    cards = shuffle_cards
print(cards)
