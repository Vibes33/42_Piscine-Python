def validate_ingredients(ingredients: str) -> str:
    """Validates spell ingredients."""
    valid_elements = ["fire", "water", "earth", "air"]
    words = ingredients.lower().split()
    if any(elem in words for elem in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
