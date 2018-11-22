# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

"""
Permutation is an arrangement of objects in a specific order. 
Order of arrangement of object is very important. 
The number of permutations on a set of n elements is given by  n!.  
For example, there are 2! = 2*1 = 2 permutations of {1, 2}, namely {1, 2} and {2, 1}, 
and 3! = 3*2*1 = 6 permutations of {1, 2, 3}, namely {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2, 1}.
"""

#############
# Method 1  #
#############
# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
data = list('123') 
for p in permutation(data): 
    print(p)

###################
# Direct Function #
###################
from itertools import permutations 
l = list(permutations(range(1, 4))) 
print(l)
