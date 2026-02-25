from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmutes lead to gold using fire."""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Transmutes stone to gem using earth."""
    return f"Stone transmuted to gem using {create_earth()}"
