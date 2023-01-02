boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Sarah']
boys.sort()
girls.sort()
if len(boys) != len(girls):
    print("Количество М и Ж не совпадает")
    exit(1)
else:
    print("Идеальные пары: ")
    for i in range(0, len(girls) - 1):
        print(boys[i], "и", girls[i])
