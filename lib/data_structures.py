spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    result_list = list()
    for entry in spicy_foods:
        result_list.append(entry.get('name'))
    return result_list

def get_spiciest_foods(spicy_foods):
    pass
    result_list = list()
    for entry in spicy_foods:
        if entry.get('heat_level') > 5:
            result_list.append(entry)
    return result_list

def print_spicy_foods(spicy_foods):
    pass
    for entry in spicy_foods:
        print(f"{entry['name']} ({entry['cuisine']}) | Heat Level: {entry['heat_level'] * '🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for entry in spicy_foods:
        if cuisine == entry['cuisine']:
            return entry


def print_spiciest_foods(spicy_foods):
    pass
    for entry in spicy_foods:
        if entry['heat_level'] > 5:
            print(f"{entry['name']} ({entry['cuisine']}) | Heat Level: {entry['heat_level'] * '🌶'}")

def get_average_heat_level(spicy_foods):
    pass
    result = 0
    for entry in spicy_foods:
        result += entry['heat_level']
    return result / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods

