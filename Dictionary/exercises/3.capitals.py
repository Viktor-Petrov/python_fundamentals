country = input().split(", ")
capital = input().split(", ")

# mydict = {}
#
# for i in range(len(country)):
#     mydict[country[i]] = capital[i]
# for key, value in mydict.items():
#     print(f"{key} -> {value}")

result = {country[i]: capital[i] for i in range(len(country))}
for key, value in result.items():
    print(f"{key} -> {value}")