import requests
import json


def get_item_prices(item):
    prices = {}
    database = requests.get("https://pangeayt2.eu/offshop_exchange_stat.php").json()  # get all the data from api

    data = database[item]  # find in the response from api item that we are looking for

    # iter through the week (last 7 days)
    for date in data:
        data[date] = data[date]["g"]  # left the price in gold

    prices[item] = data  # add item prices to prices with all inputted items

    return prices


def get_latest_price(prices):
    price_pairs = list(prices.values())[0]
    raw_prices = list(price_pairs.values())
    latest_price = raw_prices[-1]

    return latest_price
        

def get_recipes(item):
    with open("recipes.json", encoding="utf-8") as recipes_file:
        recipes_json = json.load(recipes_file)

    for product in recipes_json:
        if product["item_name"] == item:
            recipes = product["recipes"]

            return recipes


def calculate_recipe(recipe):
    calculated_recipe = {
        "recipe_name": recipe["recipe_name"],
        "item_price": "",
        "recipe_price": ""
    }
    recipe_price = 0
    ingredients = recipe["ingredients"]

    for item in ingredients.items():
        item_prices = get_item_prices(item[0])
        latest_price = get_latest_price(item_prices)

        recipe_price += latest_price * item[1]

    calculated_recipe["item_price"] = recipe_price / recipe["product_amount"]
    calculated_recipe["recipe_price"] = recipe_price

    return calculated_recipe
