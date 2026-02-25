def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level descending using lambda."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages with power >= min_power using lambda."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '* ' prefix and ' *' suffix to each spell using lambda."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate power statistics using lambdas."""
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Cloak', 'power': 78, 'type': 'armor'},
    ]

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    mages = [
        {'name': 'Merlin', 'power': 95, 'element': 'arcane'},
        {'name': 'Gandalf', 'power': 88, 'element': 'light'},
        {'name': 'Novice', 'power': 30, 'element': 'fire'},
    ]

    print("\nTesting power filter...")
    strong = power_filter(mages, 50)
    print(f"Mages with power >= 50: {[m['name'] for m in strong]}")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']}")
