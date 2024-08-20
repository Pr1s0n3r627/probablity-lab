'''
in a list mol = [I, am, writing, a, program]. randomly sample 1500 words and print the frequncy of each wprd in dictionary for as {i: freq, am:freq...} when

a seed = 30
b seed = 40
'''

import numpy as np

def sample_and_count_frequency(words, seed_value):
    # Set the seed for reproducibility
    np.random.seed(seed_value)
    
    # Sample 1500 words with replacement from the list
    sampled_words = np.random.choice(words, 1500, replace=True)
    
    # Initialize a dictionary to count the frequency of each word
    frequency_dict = {word: 0 for word in words}
    
    # Count the frequency of each word in the sampled list
    for word in sampled_words:
        frequency_dict[word] += 1
    
    return frequency_dict

# List of words to sample from
mol = ['I', 'am', 'writing', 'a', 'program']

# Sample and print frequency with seed = 30
freq_seed_30 = sample_and_count_frequency(mol, 30)
print("Frequencies with seed 30:")
print(freq_seed_30)

# Sample and print frequency with seed = 40
freq_seed_40 = sample_and_count_frequency(mol, 40)
print("\nFrequencies with seed 40:")
print(freq_seed_40)
