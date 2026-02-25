import functools
import time


def spell_timer(func: callable) -> callable:
    """Decorator that measures function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates the first argument >= min_power."""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0] if args else kwargs.get('power', 0)
            # skip 'self' if it's a bound method call
            if args and hasattr(args[0], '__class__') and not isinstance(args[0], (int, float)):
                power = args[1] if len(args) > 1 else kwargs.get('power', 0)
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries on exception up to max_attempts times."""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return (f"Spell casting failed after "
                    f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    """Guild class demonstrating staticmethod and decorators."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check name is >= 3 chars and only letters/spaces."""
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with power validation."""
        if power < 10:
            return "Insufficient power for this spell"
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(min_power=20)
    def lightning(power):
        return f"Lightning with {power} power"

    print(lightning(50))
    print(lightning(5))

    print("\nTesting retry spell...")
    counter = {"n": 0}

    @retry_spell(max_attempts=3)
    def unstable_spell():
        counter["n"] += 1
        if counter["n"] < 3:
            raise RuntimeError("Spell unstable!")
        return "Spell succeeded!"

    print(f"Result: {unstable_spell()}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Ab"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
