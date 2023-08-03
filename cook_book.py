with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for _ in range(ing_count):
            ing = file.readline()
            ing_name, q, m = ing.strip().split(' | ')
            ingredient = {
                'ingredient_name' : ing_name,
                'quantity' : q,
                'measure' : m
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[dish_name] = ingredients


def ingredient_list_for_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in result:
                    result[ing['ingredient_name']]['quantity'] \
                        += int(ing['quantity']) * person_count
                else:
                    result[ing['ingredient_name']] = \
                    {'measure': ing['measure'],
                     'quantity': int(ing['quantity']) * person_count}
        else:
            return 'Блюда нет в книге рецептов'
    return result