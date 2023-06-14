first_sequance = input().split()
sequance = "".join(first_sequance)
mydict = {}

for ch in sequance:
    if ch not in mydict.keys():
        mydict[ch] = 0
    mydict[ch] += 1

for key, lavue in mydict.items():
    print(f"{key} -> {lavue}")