import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str):
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str):
        with open(source_path, newline="") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                quantity = int(row[3])

                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                plate = next(
                    (d for d in self.dishes if d.name == dish_name),
                    None,
                )
                if plate is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, quantity)
