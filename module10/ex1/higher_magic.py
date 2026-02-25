def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Return a function that calls both spells and returns a tuple."""
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Return a function that multiplies the spell's result."""
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Return a function that casts spell only if condition is True."""
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """Return a function that casts all spells and returns results list."""
    def sequence(*args, **kwargs):
        return [s(*args, **kwargs) for s in spells]
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    fireball = lambda target: f"Fireball hits {target}"
    heal = lambda target: f"Heals {target}"
    combined = spell_combiner(fireball, heal)
    r = combined("Dragon")
    print(f"Combined spell result: {r[0]}, {r[1]}")

    print("\nTesting power amplifier...")
    base = lambda: 10
    amplified = power_amplifier(base, 3)
    print(f"Original: {base()}, Amplified: {amplified()}")

    print("\nTesting conditional caster...")
    is_enemy = lambda t: t == "Enemy"
    attack = lambda t: f"Attacking {t}"
    cond = conditional_caster(is_enemy, attack)
    print(f"Enemy: {cond('Enemy')}")
    print(f"Ally: {cond('Ally')}")

    print("\nTesting spell sequence...")
    spells = [
        lambda t: f"Fireball on {t}",
        lambda t: f"Frost on {t}",
        lambda t: f"Heal on {t}",
    ]
    seq = spell_sequence(spells)
    print(f"Sequence: {seq('Target')}")
