from abc import ABC, abstractmethod


class Dish(ABC):
    @abstractmethod
    def serve(self):
        pass


class Risotto(Dish):
    def serve(self):
        return "Risotto is ready!"


class Pasta(Dish):
    def serve(self):
        return "Pasta is ready!"


class Pizza(Dish):
    def serve(self):
        return "Pizza is ready!"


class OrderPart:
    def get_dish(self, dish_type):
        if dish_type == "risotto":
            return Risotto()
        elif dish_type == "pasta":
            return Pasta()
        elif dish_type == "pizza":
            return Pizza()
        else:
            raise ValueError("Unknown dish type")


order_part = OrderPart()
dish = order_part.get_dish("pizza")
print(dish.serve())
