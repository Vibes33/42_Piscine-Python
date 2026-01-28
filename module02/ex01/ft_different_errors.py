
def garden_operations(task):
    """
    Performs risky garden operations that might raise exceptions.
    Used to demonstrate different error types.
    """
    if task == "input":
        # Simulating bad user input
        return int("abc")
    elif task == "calculation":
        # Simulating bad math
        return 10 / 0
    elif task == "file":
        # Simulating missing file
        f = open("missing.txt", "r")
        f.close()
    elif task == "lookup":
        # Simulating missing plant data
        inventory = {"Rose": 25}
        return inventory["missing_plant"]

def test_error_types():
    print("=== Garden Error Types Demo ===")

    # 1. ValueError
    print("Testing ValueError...")
    try:
        garden_operations("input")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # 2. ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("calculation")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    # 3. FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    # 4. KeyError
    print("Testing KeyError...")
    try:
        garden_operations("lookup")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    # 5. Multiple errors together
    print("Testing multiple errors together...")
    try:
        # We can trigger any error here to test the catch-all
        garden_operations("input")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
