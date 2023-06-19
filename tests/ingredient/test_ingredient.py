from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient(self):
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")

    hash1 = hash(ingredient1)
    hash2 = hash(ingredient2)

    assert hash1 == hash2

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")

    hash1 = hash(ingredient1)
    hash2 = hash(ingredient2)

    assert hash1 != hash2

    ingredient = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert ingredient.restrictions == expected_restrictions
    assert ingredient2 != expected_restrictions
