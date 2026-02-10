# 1. Custom Exceptions
class GardenError(Exception):
    """Base garden error"""
    pass

class PlantError(GardenError):
    """Raised for issues with specific plants"""
    pass

class WaterError(GardenError):
    """Raised for watering issues"""
    pass

# 2. Main Manager Class
class GardenManager:
    def __init__(self):
        self.plants = []
        self.water_tank_level = 20 #Liters

    def add_plant(self, name):
        """Adds a plant to the garden. Raises PlantError if name is invalid."""
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")

            self.plants.append(name)
            print(f"Added {name} successfully")

        except PlantError as e:
            # We catch it here to print a message, but we could also let it bubble up
            print(f"Error adding plant: {e}")

    def water_all_plants(self):
        """Demonstrates finally block usage"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                # Simulate water usage
                if self.water_tank_level < 5:
                    raise WaterError("Not enough water in tank")
                
                self.water_tank_level -= 5
                print(f"Watering {plant} - success")
                
        except WaterError as e:
            print(f"Caught GardenError: {e}")
            
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant, water_level, sun_hours):
        """Demonstrates validation logic raising errors"""
        # This method assumes the caller handles the errors (no try/except inside)
        if water_level > 10:
             raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sun_hours < 2:
             raise PlantError(f"Sunlight {sun_hours} is too low (min 2)")
             
        print(f"{plant}: healthy (water: {water_level}, sun: {sun_hours})")

# 3. Test Function
def test_garden_management():
    print("=== Garden Management System ===")
    
    manager = GardenManager()
    
    # 1. Adding Plants (Validation)
    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("") # Should trigger error but continue
    
    # 2. Watering (Finally block)
    print("\nWatering plants...")
    manager.water_all_plants()
    
    # 3. Health Checks (Raising and Catching)
    print("\nChecking plant health...")
    # Good case
    try:
        manager.check_health("tomato", 5, 8)
    except GardenError as e:
        print(f"Error checking tomato: {e}")
    # Bad case
    try:
        manager.check_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    # 4. Error Recovery Demo
    print("\nTesting error recovery...")
    # Drain the tank manually to force an error
    manager.water_tank_level = 0
    manager.water_all_plants() # Should catch error and recover
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management()
