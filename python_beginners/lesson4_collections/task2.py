"""Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]
"""

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

x = []
uniq = []
for id in ids.values():
    x.extend(id)

for num in x:
    if num in uniq:
        continue
    else:
        uniq.append(num)
print(uniq)
print(list(set(x)))