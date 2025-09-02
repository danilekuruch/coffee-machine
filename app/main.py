import copy
from typing import List
from enums.ingredient_type import IngredientType
from enums.ingredient_measurement import IngredientMeasurement
from models.coffee import BaseCoffeeRecipe, EspressoCoffeeRecipe, LatteCoffeeRecipe, CappuccinoCoffeeRecipe
from models.ingredient_tank import IngredientTank


class CoffeeMachine:
    def __init__(self) -> None:
        self._recipes: List[BaseCoffeeRecipe] = [
            EspressoCoffeeRecipe(), LatteCoffeeRecipe(), CappuccinoCoffeeRecipe()
        ]
        self._tanks: dict[IngredientType, IngredientTank] = {
            IngredientType.water: IngredientTank(IngredientType.water, 400),
            IngredientType.milk: IngredientTank(IngredientType.milk, 540),
            IngredientType.coffee_beans: IngredientTank(IngredientType.coffee_beans, 120),
        }
        self._bank_account: int = 550
        self._disposable_cups: int = 9

    def fill(self):
        for ingredient_type, tank in self._tanks.items():
            ingredient_measurement = IngredientMeasurement[ingredient_type.name]
            msg = f"Write how many {ingredient_measurement.loc} of {ingredient_type.name} the coffee machine has:"
            self._tanks[ingredient_type].value += int(input(msg))

        user_input = input("Write how many disposable cups you want to add: ")
        self._disposable_cups += int(user_input)

    def calculate_possible_cups(self, recipe: BaseCoffeeRecipe) -> int:
        cur_tank = copy.deepcopy(self._tanks)
        amount = 0
        while all(cur_tank[i_type].value >= requirement.value for i_type, requirement in recipe.ingredients.items()):
            for ingredient in recipe.ingredients:
                cur_tank[ingredient].value -= ingredient.value
            amount += 1
        return amount

    def buy(self):
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if user_input == "back":
            return
        recipe_index = int(user_input)
        if recipe_index < 1 or recipe_index > 3:
            return

        recipe = self._recipes[recipe_index - 1]
        if self.calculate_possible_cups(recipe) <= 0:
            self.print_missed_ingredients(recipe)
            return

        for ingredient_type, ingredient_requirement in recipe.ingredients.items():
            self._tanks[ingredient_type].value -= ingredient_requirement.value
        self._bank_account += recipe.price
        self._disposable_cups -= 1

    def print_missed_ingredients(self, recipe: BaseCoffeeRecipe):
        for ingredient_type, ingredient in recipe.ingredients.items():
            if self._tanks[ingredient_type].value < ingredient.value:
                print(f"Sorry, not enough {ingredient_type.name}!")
                break

    def take(self, amount: int = 0):
        if amount == 0:
            amount = self._bank_account
        print(f"I gave you ${amount}")
        self._bank_account -= amount

    @property
    def possible_actions(self):
        return {
            "buy": self.buy,
            "fill": self.fill,
            "take": self.take,
            "exit": exit,
            "remaining": self.print_statistic
        }

    def statistic(self):
        return [
            "The coffee machine has:",
            *[
                f"{tank.value} {IngredientMeasurement[ingredient_type.name].value} of {ingredient_type.name}"
                for ingredient_type, tank in self._tanks.items()
            ],
            f"{self._disposable_cups} disposable cups",
            f"${int(self._bank_account)} of money"
        ]

    def print_statistic(self):
        print("\n" + "\n".join(self.statistic()) + "\n")


def main():
    coffee_machine = CoffeeMachine()

    possible_actions = ", ".join(coffee_machine.possible_actions.keys())
    while action := input(f"Write action ({possible_actions})"):
        try:
            coffee_machine.possible_actions[action]()
        except ValueError:
            print(f"{action} is not a valid action")


if __name__ == "__main__":
    main()
