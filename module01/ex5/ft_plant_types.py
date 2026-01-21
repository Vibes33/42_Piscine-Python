class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = (self.trunk_diameter * self.height) / 300 
        print(f"{self.name} provides {int(shade_area)} square meters of shade")

    def get_info(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"

if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 14, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 10, 60, "autumn", "beta-carotene")

    # Flowers
    print(rose.get_info())
    rose.bloom()
    print(tulip.get_info())
    tulip.bloom()
    print()

    # Trees
    print(oak.get_info())
    oak.produce_shade()
    print(pine.get_info())
    pine.produce_shade()
    print()

    # Vegetables
    print(tomato.get_info())
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print(carrot.get_info())
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")
