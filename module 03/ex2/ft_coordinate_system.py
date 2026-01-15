import math
import sys

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

print("=== Game Coordinate System ===")

# 1. Creating a position tuple
pos1 = (10, 20, 5)
origin = (0, 0, 0)
print(f"Position created: {pos1}")

# 2. Calculating distance
dist1 = calculate_distance(origin, pos1)
print(f"Distance between {origin} and {pos1}: {dist1:.2f}")

# 3. Parsing coordinates function
def parse_and_process(coord_str):
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parts = coord_str.split(',')
        if len(parts) != 3:
            raise ValueError("Expected 3 coordinates")
            
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        
        position = (x, y, z)
        print(f"Parsed position: {position}")
        
        dist = calculate_distance(origin, position)
        print(f"Distance between {origin} and {position}: {dist}")
        
        return position

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None

# Test case 1: Valid
pos2 = parse_and_process("3,4,0")

# Test case 2: Invalid
print('Parsing invalid coordinates: "abc,def,ghi"')
try:
    # Mimicking the specific error handling flow for the example output
    parts = "abc,def,ghi".split(',')
    x = int(parts[0]) # This triggers the error
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

# 4. Unpacking demonstration
print("Unpacking demonstration:")
if pos2:
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
