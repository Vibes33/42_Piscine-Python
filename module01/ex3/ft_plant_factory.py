class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def plant_factory():
    plant_blueprints = [
        ("Rose", "25cm", 30),
        ("Oak", "200cm", 365),
        ("Cactus", "5cm", 90),
        ("Sunflower", "80cm", 45),
        ("Fern", "15cm", 120)
    ]

    print("=== Plant Factory Output ===")
    
    plants = []
    for name, height, age in plant_blueprints:
        new_plant = Plant(name, height, age)
        plants.append(new_plant)
        print(f"Created: {new_plant.name} ({new_plant.height}, {new_plant.age} days)")

    print(f"Total plants created: {len(plants)}")

if __name__ == "__main__":
    plant_factory()
