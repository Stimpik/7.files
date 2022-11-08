def reading_book(book):
    with open(book, 'r', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            count = int(f.readline())
            ingr = []
            for _ in range(count):
                ingtidient = f.readline().split(' | ')
                ingredient_name, quantity, measure = ingtidient
                ingridients = {'ingredient_name': ingredient_name,
                               'quantity': quantity,
                               'measure': measure.strip()}
                ingr.append(ingridients)
            dishs = {line.strip(): ingr}
            cook_book.update(dishs)
            f.readline()
        return cook_book


def get_shop_list_by_dishes(cook_book, person_count):
    result = {}
    for dish in cook_book.values():
        temporary_dict = {}
        for ingtidient in dish:
            if ingtidient['ingredient_name'] in result:
                ingtidient['quantity'] = int(ingtidient['quantity']) * person_count
                result[ingtidient['ingredient_name']]['quantity'] += ingtidient['quantity']
            else:
                ingtidient['quantity'] = int(ingtidient['quantity']) * person_count
                temporary_dict = {ingtidient.pop('ingredient_name'): {'measure': ingtidient['measure'],
                                                                      'quantity': (ingtidient['quantity'])}}
                result.update(temporary_dict)
    return result


# print(get_shop_list_by_dishes(reading_book('recept.txt'), 2))
