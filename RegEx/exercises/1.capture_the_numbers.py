import re
#
# words = input()
# numbers = []
#
# while words:
#     pattern = "\d+"
#     matches = re.findall(pattern, words)
#     numbers.append(matches)
#     words = input()
# for num in numbers:
#     if num != []:
#      print(" ".join(num), end=" ")


pattern = '\d+'
line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        print(' '.join(matches), end = " ")
    line = input()



