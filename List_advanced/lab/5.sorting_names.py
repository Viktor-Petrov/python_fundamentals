names = input().split(', ')
sortedlst = sorted(names, key=lambda x: (-len(x), x))
print(sortedlst)
