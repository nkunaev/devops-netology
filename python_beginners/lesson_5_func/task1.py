# Каталог документов хранится в следующем виде:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

"""
TASK # 1

Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.

l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
 владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь
  будет пытаться добавить документ на несуществующую полку.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное 
название, передающие её действие.
"""




def add_list(): #add
    print("Это раздрел для добавления нового документа в каталог и полку", "\n")
    new_doc = {
        "type": input("Введите тип документа: "), "number": input("Введите номер документа: "),
        "name": input("Введите имя и фамилию владельца документа: ")
               }
    while True:
        new_shelf = input("Введите номер полки, на которой будет храниться документ: или 'q' для отмены ")
        if new_shelf in directories.keys():
            documents.append(new_doc)
            directories[new_shelf].append(new_doc["number"])
            break
        elif new_shelf == "q":
            break
        else:
            print("Такой полки не существует, выбери № 1-3 ")
    print(f"Добавлен новый доумент {new_doc}, который хранится на полке № {new_shelf} ")
    print(documents, "\n", directories, "\n")
    return exit(0)

add_list()


def doc_list(my_dict: dict):  # l
    print("Это раздел для вывода данных в формате passport '2207 876234'Василий Гупкин'", "\n")
    my_list = []
    for doc in my_dict:
        my_list.append(doc['type'])
        my_list.append(doc['number'])
        my_list.append(doc['name'])
        return my_list


def doc_where(my_dict: dict):  # s
    print("Это раздел для поиска местонахождения документа", "\n")
    doc_number = input("Введите номер документа: ")
    if doc_number is None:
        return print("Enter doc number")
    for shelf, num in my_dict.items():
        if doc_number in num:
            return shelf
        else:
            return "Такого документа нет"


def doc_whois(my_dict):  # p
    print("Это раздел для поиска человека по номеру документа", "\n")
    doc_number = input("Введите номер документа: ")
    if doc_number is None:
        return print("Enter doc number")
    for num in my_dict:
        if num["number"] == doc_number:
            return num["name"]
        else:
            return "There is no person with this doc number"
