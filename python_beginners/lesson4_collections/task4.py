'''
Дана статистика рекламных каналов по объемам продаж.
Напишите скрипт, который возвращает название канала с максимальным объемом.
Т.е. в данном примере скрипт должен возвращать 'yandex'.
'''

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def statistics(diction):
    max_amount = -1
    leader = -1
    for company, sales in diction.items():
            if sales > max_amount:
                max_amount = sales
                leader = company
    return print(f"Компания с максимальным объемом это - {leader.capitalize()}")

statistics(stats)