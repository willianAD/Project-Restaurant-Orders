import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()

    def load_menu_data(self):
        with open(self.source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                quantity = int(row[3])

                plate = next(
                    (d for d in self.dishes if d.name == dish_name),
                    None,
                )
                if plate is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(plate)
                    ingredient = Ingredient(ingredient_name)

                    dish.add_ingredient_dependency(ingredient, quantity)
