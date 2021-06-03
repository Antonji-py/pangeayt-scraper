import sys
from pangeayt import *


item_name = sys.argv[1]
recipes = get_recipes(item_to_found)

for recipe in recipes:
    recipe_price = calculate_recipe(recipe)
    print(recipe_price)
