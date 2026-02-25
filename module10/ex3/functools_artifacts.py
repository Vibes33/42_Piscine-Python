import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using functools.reduce and operator module."""
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create partial applications for different element enchantments."""
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, "fire"),
        'ice_enchant': functools.partial(base_enchantment, 50, "ice"),
        'lightning_enchant': functools.partial(
            base_enchantment, 50, "lightning"
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Cached fibonacci using lru_cache."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Create a singledispatch spell system."""
    @functools.singledispatch
    def cast(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register(int)
    def _(spell):
        return f"Damage spell: {spell} damage dealt"

    @cast.register(str)
    def _(spell):
        return f"Enchantment: {spell} applied"

    @cast.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells launched"

    return cast


if __name__ == "__main__":
    powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")
    def enchant(power, element, target):
        return f"{element.title()} enchantment ({power}p) on {target}"

    enchants = partial_enchanter(enchant)
    print(enchants['fire_enchant']("Sword"))
    print(enchants['ice_enchant']("Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(50))
    print(cast("Fireball"))
    print(cast([1, 2, 3]))
