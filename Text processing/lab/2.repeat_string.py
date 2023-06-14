sequence = input().split()
multiply_word = []

for word in sequence:
    multiply_word.append(word * len(word))
print("".join(multiply_word))