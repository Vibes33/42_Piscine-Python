def mage_counter() -> callable:
    """Return a function that counts how many times it's been called."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Return a function that accumulates power over time."""
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a function that applies the enchantment to an item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    """Return store/recall functions sharing a private memory dict."""
    memory = {}

    def store(key: str, value) -> None:
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Add 50: {acc(50)}")
    print(f"Add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("spell", "Fireball")
    print(f"Recall spell: {vault['recall']('spell')}")
    print(f"Recall unknown: {vault['recall']('unknown')}")
