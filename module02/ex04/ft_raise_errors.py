def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validates plant condition parameters.
    Raises ValueError if any parameter is out of bounds.
    """
    
    # 1. Check Name
    if not plant_name: # Empty string is Falsy in Python
        raise ValueError("Plant name cannot be empty!")
        
    # 2. Check Water Level
    if water_level < 1 or water_level > 10:
        if water_level > 10:
            msg = f"Water level {water_level} is too high (max 10)"
        else:
            msg = f"Water level {water_level} is too low (min 1)"
        raise ValueError(msg)
        
    # 3. Check Sunlight
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours > 12:
            msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        else:
            msg = f"Sunlight hours {sunlight_hours} is too low (min 2)"
        raise ValueError(msg)
        
    # If all checks pass
    return f"Plant '{plant_name}' is healthy!"

def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    # 1. Good Case
    print("Testing good values...")
    try:
        msg = check_plant_health("tomato", 5, 6)
        print(msg)
    except ValueError as e:
        print(f"Unexpected error: {e}")

    # 2. Bad Name
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    # 3. Bad Water
    print("Testing bad water level...")
    try:
        check_plant_health("cactus", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    # 4. Bad Sunlight
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("fern", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()
