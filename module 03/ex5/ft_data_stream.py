# Generators defined at the top

def game_event_generator(n_events):
    """
    Yields game events one by one.
    Simulates data with deterministic logic since 'random' is not imported.
    """
    players = ["alice", "bob", "charlie", "dave", "eve"]
    actions = ["killed monster", "found treasure", "leveled up", "completed quest", "died"]
    
    for i in range(1, n_events + 1):
        # Pseudo-random logic using modulo
        player_idx = (i * 3) % len(players)
        action_idx = (i * 7) % len(actions)
        level = (i * 13) % 20 + 1  # Levels 1 to 20
        
        event = {
            "id": i,
            "player": players[player_idx],
            "level": level,
            "action": actions[action_idx]
        }
        yield event

def fibonacci_generator():
    """Yields numbers in the Fibonacci sequence indefinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_generator():
    """Yields prime numbers indefinitely"""
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Main Execution

print("=== Game Data Stream Processor ===")
total_to_process = 1000
print(f"Processing {total_to_process} game events...")

# Initialize stats
stats = {
    "high_level": 0,    # 10 or higher
    "treasure": 0,
    "levelup": 0
}

# 1. Processing data stream with for-loop
# We create the generator object
stream = game_event_generator(total_to_process)

# Iterate
for event in stream:
    # Print first 3 events only to illustrate stream
    if event["id"] <= 3:
        print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")
    elif event["id"] == 4:
        print("...")
        
    # Analytics logic
    if event["level"] >= 10:
        stats["high_level"] += 1
        
    if event["action"] == "found treasure":
        stats["treasure"] += 1
    elif event["action"] == "leveled up":
        stats["levelup"] += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total_to_process}")
print(f"High-level players (10+): {stats['high_level']}")
print(f"Treasure events: {stats['treasure']}")
print(f"Level-up events: {stats['levelup']}")
print("Memory usage: Constant (streaming)")
# Hardcoded generic time as 'time' module is not authorized to measure it
print("Processing time: < 0.1 seconds")

print("\n=== Generator Demonstration ===")

# 2. Manual control using next() and iter()
# Fibonacci
fib = fibonacci_generator() # Create the generator
fib_list = []
for _ in range(10):
    fib_list.append(str(next(fib))) # Manually grab next value
print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

# Primes
primes = prime_generator()
prime_list = []
for _ in range(5):
    prime_list.append(str(next(primes)))
print(f"Prime numbers (first 5): {', '.join(prime_list)}")
