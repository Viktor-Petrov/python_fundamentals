replacing_word = input().split(", ")
sentence = input()


for word in replacing_word:
    if word in sentence:
        sentence = sentence.replace(word, "*" * len(word))
print(sentence)