'''
generate 1500 integers between (90, 100). 
print the frequency in the dictionary as 
{number : frequency} of all numbers i.e.
90 to 100 while selecting the seed as 

a. when seed value is 2
b. when seed value is 4
c. when seed value is 6
'''

import numpy as np

def generate_and_count(seed_value):
    # seed 
    np.random.seed(seed_value)
    
    # 1500 random integers between 90 and 100 
    random_integers = np.random.randint(90, 101, 1500)
    
    # Initialize dictionary
    frequency_dict = {}
    for number in range(90, 101):
        frequency_dict[number] = 0
    
    # Count the frequency 
    for number in random_integers:
        frequency_dict[number] += 1
    
    return frequency_dict

# printing for seed value 2 , 4 and 6
for seed in [2, 4, 6]:
    frequency = generate_and_count(seed)
    print(f"Frequency with seed {seed}:")
    print(frequency)
    print("\n")
