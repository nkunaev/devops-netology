def to_cook_book():
    ST_TITLE = 1
    ST_COUNT = 2
    ST_ING = 3
    stage = ST_TITLE
    cook_book = {}

    with open('recipe.txt', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue

            if stage == ST_TITLE:
                title = line
                cook_book[title]=[]
                stage=ST_COUNT

            elif stage == ST_COUNT:
                count = int(line)
                stage = ST_ING

            else:
                data = [x.strip() for x in line.split('|')]
                data[1] = int(data[1])
                cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
                count -= 1
                if count == 0:
                    stage = ST_TITLE
    return cook_book

book = to_cook_book()

with open('cook_book.py', 'w', encoding='utf-8') as f:
    f.write('cook_book = ')
    for key, val in book.items():
        f.writelines(f"{key}:{val}'\n'")