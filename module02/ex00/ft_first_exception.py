def check_temperature(temp_str):
    """
    Validates a temperature reading.
    Returns the integer temperature if valid, None otherwise.
    Hanles exceptions for non-numeric input.
    """
    try:
        # 1. Attempt to convert string to number
        # This will raise a ValueError if temp_str is not a number (like "abc")
        temp = int(temp_str)
        
        # 2. Check bounds (Logic validation)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        else:
            # 3. Success case
            return temp

    except ValueError:
        # 4. Error Handler for non-numeric strings
        print(f"Error: '{temp_str}' is not a valid number")
        return None

def test_temperature_input():
    """
    Simulates a data pipeline receiving various inputs
    """
    print("=== Garden Temperature Checker ===")
    
    # List of simulated sensor data
    sensor_data = ["25", "abc", "100", "-50"]
    
    for reading in sensor_data:
        print(f"Testing temperature: {reading}")
        
        # Call the validation function
        valid_temp = check_temperature(reading)
        
        # If we got a result back (not None), it's safe to use
        if valid_temp is not None:
            print(f"Temperature {valid_temp}°C is perfect for plants!")
            
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
