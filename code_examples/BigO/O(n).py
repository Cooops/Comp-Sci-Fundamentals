# O(n)
def string_length(strng):
    """
    This algorithm is said to run in linear time with respect to the number of characters (n) in the string. 
    In short, it runs in O(n); the time required to traverse the entire string is proportional to the number of characters. 

    20 characters take twice as long as 10 characters, etc. 
    As you increase the number of characters, the runtime will increase linearly with the input length.
    
    O(n) steps = O(n) in total.
    """
    counter = 0
    for character in strng:
        counter += 1
    return counter