import copy
from app.enums.ingredient_type import IngredientType
from app.models.ingredient_requirement import IngredientRequirement, DEFAULT_COFFEE_REQUIREMENTS


class BaseCoffeeRecipe:
    def __init__(self, price: int, ingredients: dict[IngredientType, IngredientRequirement] = None):
        if ingredients is None:
            ingredients = copy.deepcopy(DEFAULT_COFFEE_REQUIREMENTS)
        self.ingredients = ingredients
        self.price = price


class EspressoCoffeeRecipe(BaseCoffeeRecipe):
    def __init__(self):
        super().__init__(4)


class LatteCoffeeRecipe(BaseCoffeeRecipe):
    def __init__(self):
        super().__init__(7)
        self.ingredients[IngredientType.water].value = 350
        self.ingredients[IngredientType.milk].value = 75
        self.ingredients[IngredientType.coffee_beans].value = 20


class CappuccinoCoffeeRecipe(BaseCoffeeRecipe):
    def __init__(self):
        super().__init__(6)
        self.ingredients[IngredientType.water].value = 200
        self.ingredients[IngredientType.milk].value = 100
        self.ingredients[IngredientType.coffee_beans].value = 12
