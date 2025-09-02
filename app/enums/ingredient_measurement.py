from enum import Enum


class IngredientMeasurement(Enum):
    water = "ml"
    milk = "ml"
    coffee_beans = "g"

    def loc(self):
        try:
            return INGREDIENT_MEASUREMENT_LOC[self]
        except KeyError:
            return self.value


INGREDIENT_MEASUREMENT_LOC = {
    IngredientMeasurement.coffee_beans: "grams",
}
