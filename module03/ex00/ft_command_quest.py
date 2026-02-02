import sys

def main():
    print("=== Command Quest ===")
    
    # sys.argv contains the list of command line arguments
    # sys.argv[0] is always the name of the script itself
    
    total_args = len(sys.argv)
    
    if total_args == 1:
        # Case where only the script name is present (no external args)
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_args}")
    else:
        # Case where we have external arguments
        print(f"Program name: {sys.argv[0]}")
        
        # We subtract 1 because the first element is the script name
        print(f"Arguments received: {total_args - 1}")
        
        # Iterate starting from the second element (index 1) which is the first real argument
        # enumerate(..., 1) lets us start counting 'i' from 1 instead of 0 for display
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
            
        print(f"Total arguments: {total_args}")

if __name__ == "__main__":
    main()
