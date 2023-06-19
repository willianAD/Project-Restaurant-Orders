from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient(self):
    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo mussarela')

    hash1 = hash(ingredient1)
    hash2 = hash(ingredient2)

    self.assertEqual(hash1, hash2)


def test_ingretient_not_equal(self):
    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('bacon')

    hash1 = hash(ingredient1)
    hash2 = hash(ingredient2)

    self.assertNotEqual(hash1, hash2)
