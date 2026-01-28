def water_plants(plant_list):
    """
    Simulates a watering system that MUST be closed properly.
    Uses try/finally pattern.
    """
    print("Opening watering system")
    
    try:
        # Loop through plants
        for plant in plant_list:
            if plant is None:
                # Artificial error
                raise ValueError("Cannot water None - invalid plant!")
            
            print(f"Watering {plant}")
            
    except ValueError as e:
        # Handle the error but let the program continue
        print(f"Error: {e}")
        
    finally:
        # This block runs NO MATTER WHAT happening above
        # Even if there was a return, a crash, or a success.
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===")

    # 1. Happy Path
    print("Testing normal watering...")
    good_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_list)
    print("Watering completed successfully!")
    print() # Empty line

    # 2. Error Path
    print("Testing with error...")
    bad_list = ["tomato", None, "carrots"]
    water_plants(bad_list)
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
