'''
*Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
 (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
'''

vars = ['2018-01-01', 'yandex', 'cpc', 100]

def to_dict(list_):
    result, *rest = reversed(list_)
    for i in rest:
        result = {i: result}
    return print(result)

to_dict(vars)
