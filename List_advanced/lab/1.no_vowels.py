word = input()

vowels = ['a', 'o', 'u', 'e', 'i']
result = [i for i in word if i.lower() not in vowels]
print("".join(result))