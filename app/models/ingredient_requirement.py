from app.enums.ingredient_type import IngredientType


class IngredientRequirement:
    def __init__(self, ingredient_type: IngredientType, value: int) -> None:
        self.name = ingredient_type
        self.value = value


DEFAULT_COFFEE_REQUIREMENTS = {
    IngredientType.water: IngredientRequirement(IngredientType.water, 250),
    IngredientType.milk: IngredientRequirement(IngredientType.milk, 0),
    IngredientType.coffee_beans: IngredientRequirement(IngredientType.coffee_beans, 16),
}
