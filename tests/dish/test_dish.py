import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish1 = Dish("Lasanha Presunto", 25.90)
    dish2 = Dish("Lasanha Berinjela", 27.00)

    assert dish1.name == "Lasanha Presunto"
    assert dish1.name != "Lasanha Berinjela"

    assert dish1.price == 25.90
    assert dish1.price != 27.00

    assert dish1 == Dish("Lasanha Presunto", 25.90)
    assert dish1 != Dish("Lasanha Berinjela", 27.00)

    assert repr(dish1) == "Dish('Lasanha Presunto', R$25.90)"
    assert repr(dish2) != "Dish('Lasanha Presunto', R$25.90)"

    assert hash(dish1) == hash("Dish('Lasanha Presunto', R$25.90)")
    assert hash(dish2) != hash("Dish('Lasanha Presunto', R$25.90)")

    with pytest.raises(TypeError):
        Dish("Lasanha Presunto", "25.90")

    with pytest.raises(ValueError):
        Dish("Lasanha Presunto", -3.00)

    assert dish1.recipe.get("beringela") is None

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")

    dish1.add_ingredient_dependency(ingredient1, 15)
    dish1.add_ingredient_dependency(ingredient2, 10)

    assert dish1.get_restrictions() == expected_restrictions
    assert dish2.get_restrictions() != expected_restrictions

    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish2.get_ingredients() != {ingredient1, ingredient2}
