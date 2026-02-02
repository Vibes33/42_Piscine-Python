import sys
import math

def calculate_distance(point1, point2):
    """
    Calculates Euclidean distance between two 3D points (tuples).
    Formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def parse_coordinates(coord_string):
    """
    Parses a string "x,y,z" into a tuple (x, y, z).
    Handles parsing errors gracefully.
    """
    print(f'Parsing coordinates: "{coord_string}"')
    try:
        parts = coord_string.split(',')
        if len(parts) != 3:
            raise ValueError("Must have exactly 3 coordinates")
            
        # List comprehension to convert all parts to int
        coords = [int(p.strip()) for p in parts]
        
        # Convert list to tuple (immutable)
        return tuple(coords)
        
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        # Print detailed error info as requested
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None

def main():
    print("=== Game Coordinate System ===")
    
    # 1. Basic Tuple Creation
    spawn_point = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {spawn_point}")
    
    # 2. Distance Calculation
    dist = calculate_distance(origin, spawn_point)
    print(f"Distance between {origin} and {spawn_point}: {dist:.2f}")
    
    # 3. Parsing Valid Input
    # Simulating receiving a command like "teleport 3,4,0"
    target_pos = parse_coordinates("3,4,0")
    
    if target_pos:
        print(f"Parsed position: {target_pos}")
        dist_target = calculate_distance(origin, target_pos)
        print(f"Distance between {origin} and {target_pos}: {dist_target}")
        
    # 4. Parsing Invalid Input
    parse_coordinates("abc,def,ghi")
    
    # 5. Tuple Unpacking Demo
    if target_pos:
        print("Unpacking demonstration:")
        # Magic happens here: directly extracting values into variables
        px, py, pz = target_pos
        print(f"Player at x={px}, y={py}, z={pz}")
        print(f"Coordinates: X={px}, Y={py}, Z={pz}")

if __name__ == "__main__":
    main()
