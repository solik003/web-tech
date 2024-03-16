# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class Meal:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Meal: {self.name}, Price: {self.price}")


class Burger(Meal):
    def __init__(self):
        super().__init__("Burger", 5)


class Pizza(Meal):
    def __init__(self):
        super().__init__("Pizza", 8)


class Salad(Meal):
    def __init__(self):
        super().__init__("Salad", 4)


class MealFactory:
    def create_meal(self, type):
        if type == "burger":
            return Burger()
        elif type == "pizza":
            return Pizza()
        elif type == "salad":
            return Salad()
        else:
            raise ValueError("Invalid meal type")


factory = MealFactory()

burger = factory.create_meal("burger")
burger.display()  # Output: Meal: Burger, Price: 5

pizza = factory.create_meal("pizza")
pizza.display()   # Output: Meal: Pizza, Price: 8

salad = factory.create_meal("salad")
salad.display()   # Output: Meal: Salad, Price: 4
