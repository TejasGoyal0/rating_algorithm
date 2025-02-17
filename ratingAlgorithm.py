import numpy as np
import matplotlib.pyplot as plt
from config import ALPHA, LAMBDA_FACTOR, RETURN_WINDOW, INITIAL_SCORE, REWARD

class TimeDecayReputation:
    def __init__(self):
        self.alpha = ALPHA
        self.lambda_factor = LAMBDA_FACTOR
        self.return_window = RETURN_WINDOW
        self.score = INITIAL_SCORE
        self.reward = REWARD
        self.first_transaction = True  # Skip first transaction effect

    def calculate_penalty(self, order_value, return_days):
        """Penalty increases with order value and return delay."""
        if return_days == 0:
            return self.reward  # Reward for no return
        base_penalty = -0.03 * order_value  # 3% of order value as base penalty
        delay_factor = 1 + self.lambda_factor * (return_days / self.return_window)
        return base_penalty * delay_factor

    def update_score(self, order_value, return_days):
        """Updates reputation score based on return behavior."""
        if self.first_transaction:
            self.first_transaction = False  # Skip the first update
            return self.score  # No change on the first order

        penalty = self.calculate_penalty(order_value, return_days)

        if return_days == 0:
            self.score += self.reward + 0.01 * order_value
        else:
            self.score = (1 - self.alpha) * self.score + self.alpha * penalty

        return self.score
