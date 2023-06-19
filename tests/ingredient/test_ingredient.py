from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")

    assert ingredient1 == Ingredient("queijo mussarela")
    assert ingredient1 != ingredient2

    assert ingredient1.name == "queijo mussarela"
    assert ingredient2.name != "queijo mussarela"

    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert repr(ingredient2) != "Ingredient('queijo mussarela')"
    assert hash(ingredient1) == hash("queijo mussarela")
    assert hash(ingredient2) != hash("queijo mussarela")

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert ingredient1.restrictions == expected_restrictions
    assert ingredient2.restrictions != expected_restrictions
