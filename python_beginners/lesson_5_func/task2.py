'''
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
 Предусмотрите сценарий, когда пользователь вводит несуществующий документ;

m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
 Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить
 документ на несуществующую полку;

as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай,
 когда пользователь добавляет полку, которая уже существует.;
'''

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def new_shelf():
    add_shelf = input("Введите номер новой полки: ")
    if add_shelf in directories.keys():
        print("Такая полка уже есть")
        return 0
    directories[add_shelf] = []
    print(f"Полка № {add_shelf} добавлена")
    return 0


new_shelf()


def move_func():
    doc_to_move = input("Введите номер документа и куда его переместить: ")
    count = 0
    max_count = len(directories)
    current_shelf = ""
    for key, val in directories.items():
        if doc_to_move in val:
            current_shelf = key
            print(f"Сейчас документ на после № {key}")
        elif doc_to_move not in val:
            count += 1
            if count == max_count:
                print("Такого документа нет")
                return 0
    target_shelf = input("На какую полку переместить? ")
    if target_shelf in directories.keys():
        directories[target_shelf].append(doc_to_move)
        directories[current_shelf].remove(doc_to_move)
        print(f"Документ {doc_to_move} перемещен с полки № {current_shelf} на полку № {target_shelf}")


def del_func():
    doc_to_remove = input("Введите номер документа для его удаления: ")
    max_count = len(documents)
    count = 0
    for num, doc in enumerate(documents):
        if doc_to_remove == doc["number"]:
            print(f" Документ № '{doc_to_remove}', выданный на имя '{doc['name']}' будет удален ")
            del documents[num]
            break
        elif doc_to_remove not in doc.values():
            count += 1
            if count == max_count:
                print("Такого документа нет")
                break
    for key, val in directories.items():
        if doc_to_remove in val:
            print(f"Документ {doc_to_remove} удален из полки № '{key}' ")
            val.remove(doc_to_remove)
    print(documents)
    print(directories)

    return 0
