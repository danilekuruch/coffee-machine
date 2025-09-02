from app.enums.ingredient_type import IngredientType
from app.enums.ingredient_measurement import IngredientMeasurement


class IngredientTank:
    def __init__(self, ingredient_type: IngredientType, value: int) -> None:
        self.ingredient_type = ingredient_type
        self.value = value

    @property
    def ingredient_measurement(self):
        return IngredientMeasurement(self.ingredient_type.name)
