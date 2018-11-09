# O(1)
def string_length(strng):
    """
    Lets says the above method isn't fast enough, so you may chose to store the number of characters in the string in a variable _len_, which you can then compare against instead of the checking the string itself everytime.
    Accessing len() is considered an asymptotically constant time operation, or O(1). 
    What this means is no matter how big your input is it will always take you the same amount of time to compute things (one step).
    
    O(1) steps = O(1) in total.
    """
    strngLen = len(strng)
    return strngLen