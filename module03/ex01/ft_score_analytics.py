import sys

def main():
    print("=== Player Score Analytics ===")
    
    # 1. Check if we have arguments (besides script name)
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    
    # 2. Parse arguments into integers
    # We use a loop and try/except to handle bad inputs gracefully
    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Error: '{arg}' is not a valid score. Skipping.")

    # 3. Check if we have any valid scores left after filtering
    if len(scores) == 0:
        print("No valid scores to analyze.")
        return

    # 4. Calculate Statistics
    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score
    
    # 5. Display Results
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
    main()
