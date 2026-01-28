# 1. Define Custom Exceptions
class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass

class PlantError(GardenError):
    """Raised when there is a problem with a plant"""
    pass

class WaterError(GardenError):
    """Raised when there is a water supply issue"""
    pass

# 2. Functions that raise these errors
def check_plant_health(status):
    if status == "wilting":
        raise PlantError("The tomato plant is wilting!")
    print(f"Plant is {status}")

def check_water_level(level):
    if level < 10:
        raise WaterError("Not enough water in the tank!")
    print(f"Water level: {level}L")

# 3. Test function
def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    # Test catching specific PlantError
    print("Testing PlantError...")
    try:
        check_plant_health("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    # Test catching specific WaterError
    print("Testing WaterError...")
    try:
        check_water_level(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # Test catching via the parent class (Polymorphism for errors)
    print("Testing catching all garden errors...")
    
    # Try catching a PlantError as a generic GardenError
    try:
        check_plant_health("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    # Try catching a WaterError as a generic GardenError
    try:
        check_water_level(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
