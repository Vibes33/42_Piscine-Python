class SecurePlant:
    def __init__(self, name, initial_height=0, initial_age=0):
        self._name = name
        self._height = 0
        self._age = 0

        # Use setters to initialize with validation
        self.set_height(initial_height, verbose=False)
        self.set_age(initial_age, verbose=False)
        print(f"Plant created: {self._name}")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height, verbose=True):
        if height < 0:
            if verbose:
                print(f"Invalid operation attempted: height {height}cm [REJECTED]")
                print("Security: Negative height rejected")
            return

        self._height = height
        if verbose:
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age, verbose=True):
        if age < 0:
            if verbose:
                print(f"Invalid operation attempted: age {age} days [REJECTED]")
                print("Security: Negative age rejected")
            return
            
        self._age = age
        if verbose:
            print(f"Age updated: {age} days [OK]")

    def __str__(self):
        return f"{self._name} ({self._height}cm, {self._age} days)"

if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    # Create the plant (initialized safely)
    plant = SecurePlant("Rose")

    # Update using safe methods
    plant.set_height(25)
    plant.set_age(30)

    # Attempt illegal operations
    plant.set_height(-5)
    
    # Show final state
    print(f"Current plant: {plant}")
