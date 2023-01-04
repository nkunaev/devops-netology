""" Дан список поисковых запросов. Получить распределение количества слов в них.
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д. """

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
def percent(total, amount):
    if amount == 0:
        return 0
    else:
        return float('{:.2f}'.format((amount / total) * 100))

def querry_statistics(queries):
    len_total = len(queries)
    len_1 = 0
    len_2 = 0
    len_3 = 0
    for query in queries:
        if len(query.split()) == 3:
            len_3 += 1
        elif len(query.split()) == 2:
            len_2 += 1
        elif len(query.split()) == 1:
            len_1 += 1
    result = print(f"Поисковых запросов из одного слова {percent(len_total, len_1)} %"), \
             print(f"Поисковых запросов из двух слов {percent(len_total, len_2)} %"), \
             print(f"Поисковых запросов из трех слов {percent(len_total, len_3)} %")
    return result

querry_statistics(queries)