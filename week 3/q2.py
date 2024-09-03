import random
from collections import Counter

'''
Q2. Four coins are tossed simultaneously. 
Let X denote the number of times the coin comes 
up with heads. Compute the probabilities for 
all possible values of X (within Lab).
'''

num_trials = 10000
results = []
for _ in range(num_trials):
    tosses = [random.choice(['H', 'T']) for _ in range(4)]
    num_heads = tosses.count('H')
    results.append(num_heads)

result_counts = Counter(results)
probabilities_X = {x: count / num_trials for x, count in result_counts.items()}

print("Results:")
for x, count in result_counts.items():
    print(f"X = {x}: Count = {count}, Probability = {probabilities_X[x]}")
