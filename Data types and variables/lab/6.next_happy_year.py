year = int(input())
year_is_special = False

while not year_is_special:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    year_is_special = len(set_year) == len(str(year))
print(year)

# year = int(input())
# happy_year_condition = False
#
# while not happy_year_condition:
#     year += 1
#     set_year = set()
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#
#     happy_year_condition = len(set_year) == len(str(year))
#
# print(year)
