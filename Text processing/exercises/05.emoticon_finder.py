sentence = input()

for i in range(len(sentence)):
    if sentence[i] == ":":
        print(f":{sentence[i + 1]}")


