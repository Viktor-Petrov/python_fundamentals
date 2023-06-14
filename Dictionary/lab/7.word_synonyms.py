number_of_words = int(input())
mydict = {}

for i in range(number_of_words):
    word = input()
    synonym = input()
    if word not in mydict:
        mydict[word] = []
    mydict[word].append(synonym)

for word in mydict:
    print(f'{word} - {", ".join(mydict[word])}')