'''
create a function that computes the probablity of 
some number k in a data array. 
a. if array is {20, 20, 21 ,21, 21, 22, 23 ,26 , 27, 27}
 then computer the probablity of 20 21 24 26 and 27.
b. if array is {a a b b c x y z z z}
 then compute the probablity of a d y and z
'''

import numpy as np

def compute_probability(data_array, elements):
    # data_array into numpy array
    data_array = np.array(data_array)
    
    # elements in the array
    total_elements = data_array.size
    
    # probabilities
    probability_dict = {}
    
    for element in elements:
        # occurrences
        count = np.sum(data_array == element)
        
        # probability
        probability = count / total_elements
        
        # dictionary
        probability_dict[element] = float(probability)
    
    return probability_dict

# Test case a
data_array_a = [20, 20, 21, 21, 21, 22, 23, 26, 27, 27, 28]
#elements_a = [20, 21, 24, 26, 27]
elements_a = [28]
probabilities_a = compute_probability(data_array_a, elements_a)
print("Probabilities for numeric array:", probabilities_a)

# Test case b
data_array_b = ['a', 'a', 'b', 'b', 'c', 'x', 'y', 'z', 'z', 'z']
elements_b = ['a', 'd', 'y', 'z']
probabilities_b = compute_probability(data_array_b, elements_b)
print("Probabilities for string array:", probabilities_b)
