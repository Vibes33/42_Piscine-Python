import os
import stat

def generate_data():
    print("Initializing test environment...")
    
    # Standard file
    with open("standard_archive.txt", "w") as f:
        f.write("Knowledge preserved for humanity")
    print("Created: standard_archive.txt")

    # Restricted file
    filename = "classified_vault.txt"
    with open(filename, "w") as f:
        f.write("TOP SECRET DATA")
    
    # Remove all permissions (read/write/execute) for everyone to force PermissionError
    # os.chmod works on Unix-like systems (macOS/Linux)
    try:
        os.chmod(filename, 0o000)
        print(f"Created & Locked: {filename} (Permission handling test)")
    except Exception as e:
        print(f"Warning: Could not change permissions automatically: {e}")
    
    # Ensure lost_archive doesn't exist
    if os.path.exists("lost_archive.txt"):
        os.remove("lost_archive.txt")
        print("Removed: lost_archive.txt (Missing file test)")

if __name__ == "__main__":
    generate_data()
