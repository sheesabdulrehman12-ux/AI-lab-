# Min-Max Algorithm in Python

import math

# Min-Max Function
def minimax(depth, is_maximizing):

    # Example terminal condition
    if depth == 3:
        return 0

    if is_maximizing:
        best = -math.inf

        # Simulating possible moves
        for i in range(2):
            value = minimax(depth + 1, False)
            best = max(best, value)

        return best

    else:
        best = math.inf

        # Simulating opponent moves
        for i in range(2):
            value = minimax(depth + 1, True)
            best = min(best, value)

        return best


# Main Function
result = minimax(0, True)

print("Optimal Value:", result)