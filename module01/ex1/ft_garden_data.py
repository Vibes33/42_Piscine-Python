class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    p1 = Plant("Rose", "25cm", 30)
    p2 = Plant("Sunflower", "80cm", 45)
    p3 = Plant("Cactus", "15cm", 120)

    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}, {p1.age} days old")
    print(f"{p2.name}: {p2.height}, {p2.age} days old")
    print(f"{p3.name}: {p3.height}, {p3.age} days old")
