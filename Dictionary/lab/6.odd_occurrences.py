element = input().lower().split()

mydict = {}

for word in element:
    if word not in mydict:
        mydict[word] = 0
    mydict[word] += 1
for key,value in mydict.items():
    if value % 2 != 0:
        print(key, end=" ")