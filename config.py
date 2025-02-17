# Configuration for TimeDecayReputation system
ALPHA = 0.3  # Weight for updating score (for penalties only)
LAMBDA_FACTOR = 1.25  # Penalizes late returns more
RETURN_WINDOW = 7  # Max allowed return days
INITIAL_SCORE = 10  # Initial reputation score
REWARD = 2  # Reward for no return
