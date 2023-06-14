text = input()

digit, letter, other = [], [], []

for ch in text:
    if ch.isdigit():
        digit.append(ch)
    elif ch.isalpha():
        letter.append(ch)
    else:
        other.append(ch)
print("".join(digit))
print("".join(letter))
print("".join(other))

