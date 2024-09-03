# Total balls
total_balls = 30 + 20 + 10

# Probabilities
red_probability = 30 / total_balls
blue_probability = 20 / total_balls

# Conditional probability: blue given it's blue or green
blue_or_green_probability = 20 / (20 + 10)

# Print the results
print(f"Probability of drawing a red bal l: {red_probability}")
print(f"Probability of drawing a blue ball: {blue_probability}")
print(f"Conditional probability of drawing a blue ball given it's blue or green: \n{blue_or_green_probability}")

