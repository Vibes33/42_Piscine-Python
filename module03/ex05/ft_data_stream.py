import time
import random

def game_event_generator(n_events):
    """
    Generate a stream of game events using yield.
    This is a generator function: it pauses execution and saves state between yields.
    """
    event_types = ["killed monster", "found treasure", "leveled up", "died", "joined guild"]
    names = ["alice", "bob", "charlie", "dave", "eve"]
    
    for i in range(n_events):
        name = random.choice(names)
        action = random.choice(event_types)
        level = random.randint(1, 20)

        # Yield creates the value on demand without storing the whole list list
        yield f"Player {name} (level {level}) {action}"

def fibonacci_generator():
    """Infinite stream of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_generator():
    """Infinite stream of Prime numbers."""
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

def main():
    print("=== Game Data Stream Processor ===")
    n_events = 1000
    print(f"Processing {n_events} game events...")
    
    # 1. Start the generator
    # Warning: calling the function just returns a generator object, it doesn't run code yet!
    stream = game_event_generator(n_events)
   
    # Analytics Storage
    stats = {
        "high_level": 0,
        "treasure": 0,
        "level_up": 0,
        "total": 0
    }
    start_time = time.time()
    
    # 2. Process the stream
    # The loop calls next() implicitly on the stream
    for event in stream:
        stats["total"] += 1
        
        # Simple parsing logic
        if stats["total"] <= 3:
            print(f"Event {stats['total']}: {event}")
        
        # Analyzing string content on the fly
        # "Player alice (level 5) ..."
        parts = event.split() 
        # parts[3] is "(level", parts[4] is "5)"
        try:
            level_str = parts[4].replace(")", "")
            level = int(level_str)
            if level >= 10:
                stats["high_level"] += 1
        except (ValueError, IndexError):
            pass
            
        if "found treasure" in event:
            stats["treasure"] += 1
        elif "leveled up" in event:
            stats["level_up"] += 1
            
    end_time = time.time()
    
    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.4f} seconds")
    
    print("\n=== Generator Demonstration ===")
    
    # Demo Fibonacci - Using next() manualy or islice logic
    fib = fibonacci_generator()
    fib_list = []
    for _ in range(10):
        fib_list.append(str(next(fib)))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")
    
    # Demo Primes
    prime = prime_generator()
    prime_list = []
    for _ in range(5):
        prime_list.append(str(next(prime)))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")

if __name__ == "__main__":
    main()

