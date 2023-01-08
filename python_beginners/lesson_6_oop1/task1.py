'''
гусей "Серый" и "Белый"
корову "Маньку"
овец "Барашек" и "Кудрявый"
кур "Ко-Ко" и "Кукареку"
коз "Рога" и "Копыта"
и утку "Кряква"
Со всеми животными вам необходимо как-то взаимодействовать:

кормить
корову и коз доить
овец стричь
собирать яйца у кур, утки и гусей
различать по голосам(коровы мычат, утки крякают и т.д.)
'''

from random import randrange


class Animals:
    animals = []
    def __init__(self, areal="domestic", weight=0, height=0, gender=None, name=None, voice=None):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.areal = areal
        self.name = name
        self.voice = voice


    def feed(self, food):
        print(f"Поздравляем, животное с удовольствем употребил(а) {food}")

    def call(self):
        print(f"Вы позвали {self.name}")

    def voice_(self):
        print(f"Обычно {self.name} говорит {self.voice} ")


class Goose(Animals):
    def __init__(self, name, color, voice="Га-Га-Га"):
        self.name = name
        self.color = color
        self.voice = voice
        self.animals.append(self)

    def take_egg(self):
        if self.gender == "female":
            print(f"{self.color} гусыня по кличке {self.name} принес вам {randrange(1, 15)} яиц")
        else:
            print("Пока что только гусыня можетнести яйца!")


goose_1 = Goose("Masha", "grey")
goose_1.weight = 14
goose_1.height = 31
goose_1.gender = "female"

goose_2 = Goose("Misha", "white")
goose_2.weight = 17
goose_2.height = 35
goose_2.gender = "male"


class Cow(Animals):
    def __init__(self, name, voice="Му-у-у"):
        self.name = name
        self.voice = voice
        self.animals.append(self)

    def milk(self):
        if self.gender == "female":
            print(f"{self.name} принесла {randrange(5, 20)} литров молока!")
        else:
            print("Быки пока не умеют давать молоко")


cow_1 = Cow("Манька")
cow_1.gender = "female"
cow_1.weight = 240
cow_1.height = 160


class Sheep(Animals):
    def __init__(self, name, voice="Бе-е-е"):
        self.name = name
        self.voice = voice
        self.animals.append(self)

    def cut(self):
        print(f"{self.name} безумно рад, что его подстригли!")


sheep_1 = Sheep("Барашек")
sheep_1.gender = "male"
sheep_1.weight = 45
sheep_1.height = 60

sheep_2 = Sheep("Кудрявый")
sheep_2.gender = "female"
sheep_2.weight = 31
sheep_2.height = 57


class Chicken(Animals):
    def __init__(self, name, voice="Куд-кудах"):
        self.name = name
        self.voice = voice
        self.animals.append(self)

    def take_egg(self):
        if self.gender == "female":
            print(f"Курица {self.name} принесла вам {randrange(1, 15)} яиц")
        else:
            print("Пока что только курица можетнести яйца!")


chicken_1 = Chicken("Ко-Ко")
chicken_1.gender = "female"
chicken_1.height = 32
chicken_1.weight = 17

chicken_2 = Chicken("Кукареку")
chicken_2.gender = "male"
chicken_2.height = 35
chicken_2.weight = 19


class Goat(Animals):
    def __init__(self, name, voice="Блуэ-э"):
        self.name = name
        self.voice = voice
        self.animals.append(self)

    def milk(self):
        if self.gender == "female":
            print(f"{self.name} принесла {randrange(2, 7)} литров молока!")
        else:
            print("Козлы пока не умеют давать молоко")


goat_1 = Goat("Рога")
goat_1.gender = "female"
goat_1.weight = 17
goat_1.height = 41

goat_2 = Goat("Копыта")
goat_2.gender = "male"
goat_2.weight = 21
goat_2.height = 47


class Duck(Animals):
    def __init__(self, name, voice="Кря-кря"):
        self.name = name
        self.voice = voice
        self.animals.append(self)

    def take_egg(self):
        if self.gender == "female":
            print(f"Утрка {self.name} принесла вам {randrange(1, 15)} яиц")
        else:
            print("Пока что только утка можетнести яйца!")


duck_1 = Duck("Кряква")
duck_1.gender = "female"
duck_1.height = 18
duck_1.weight = 12

def max_weight():
    animals = Animals.animals
    weight_total = []
    animals_id = []
    for i in animals:
        weight_total.append(i.weight)
        animals_id.append(i.name)
    result_id = weight_total.index(max(weight_total))
    print(f"Наибольший вес у животного по имени {animals_id[result_id]}, который составил {weight_total[result_id]} кг.")
    return 0

max_weight()