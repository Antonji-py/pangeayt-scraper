from pangeayt import *

item_name = open("item_name.txt").read()
recipes = get_recipes(item_name)

for recipe in recipes:
    recipe_price = calculate_recipe(recipe)
    print(recipe_price)
