words = input().split(' ')
palindrome = input()

palindrome_words = []
for word in words:
    if word == word[::-1]:
        palindrome_words.append(word)
print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(palindrome)} times")