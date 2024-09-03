import random
from collections import Counter

'''
Q1. From the following 
list = ["T", "am" , "Studying", "in", "BU"], 
Randomly sample 1500 words. For the word "BU" 
collect the immediate right neighbour word, 
call it as a sample space for the word "BU". 
Now compute the probability of all words in 
the sample space for the word "BU"
'''

words = ["T", "am", "Studying", "in", "BU"]
sampled_words = random.choices(words, k=1500)
sample_space = [sampled_words[i + 1] for i in range(len(sampled_words) - 1) if sampled_words[i] == "BU"]
sample_space_counter = Counter(sample_space)
total_words = len(sample_space)
probabilities = {w: c / total_words for w, c in sample_space_counter.items()}

print("Sample Space Counter:")
for word, count in sample_space_counter.items():
    print("{}: {}".format(word, count))

print("\nProbabilities:")
for word, probability in probabilities.items():
    print("{}: {:.2%}".format(word, probability))
