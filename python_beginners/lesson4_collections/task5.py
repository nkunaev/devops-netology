'''
*Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
 (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
'''

vars = ['2018-01-01', 'yandex', 'cpc', 100]

def to_dict(list_: list):
    result = list_[-1]
    for i in reversed(range(len(list_) - 1)):
        result = {list_[i]: result}
    return result

print(to_dict(vars))
print(vars[-1])
# def to_dict(list_):
#     result, *rest = reversed(list_)
#     print(result)
#     print(rest)
#     for i in rest:
#         result = {i: result}
#     return print(result)




