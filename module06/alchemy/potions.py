from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Brews a healing potion using fire and water."""
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    """Brews a strength potion using earth and fire."""
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    """Brews an invisibility potion using air and water."""
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    """Brews a wisdom potion using all four elements."""
    return (f"Wisdom potion brewed with all elements: "
            f"{create_fire()}, {create_water()}, "
            f"{create_earth()}, {create_air()}")
