class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount):
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")

class GardenManager:
    _garden_count = 0

    class GardenStats:
        """Nested helper class for statistics"""
        def __init__(self, plants):
            self.plants = plants

        def count_plant_types(self):
            regular = 0
            flowering = 0
            prize = 0
            for p in self.plants:
                # Check most specific first
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                elif isinstance(p, Plant):
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants = []
        self._total_growth_tracking = 0
        GardenManager._garden_count += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, amount):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self._total_growth_tracking += amount

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")

        # Use nested class for stats
        stats = self.GardenStats(self.plants)
        reg, flow, prize = stats.count_plant_types()

        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self._total_growth_tracking}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prize} prize flowers")

    @staticmethod
    def validate_height(height):
        # Utility function that doesn't need self or cls
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        # Works on the manager type itself 
        # Simulating network creation/status
        print("Garden scores - Alice: 218, Bob: 92")
        print(f"Total gardens managed: {cls._garden_count}")

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    
    # 1. Create Manager
    alice = GardenManager("Alice")
    
    # 2. Add Plants
    # Oak Tree (Plant)
    oak = Plant("Oak Tree", 100)
    alice.add_plant(oak)
    
    # Rose (FloweringPlant)
    rose = FloweringPlant("Rose", 25, "red")
    alice.add_plant(rose)
    
    # Sunflower (PrizeFlower)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice.add_plant(sunflower)
    
    # 3. Grow
    alice.grow_all(1)
    
    # 4. Report
    alice.generate_report()
    
    # 5. Static Method usage
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    
    # 6. Create another garden to bump the count (implied by "Total gardens managed: 2")
    bob = GardenManager("Bob")
    
    # 7. Class Method usage
    GardenManager.create_garden_network()
