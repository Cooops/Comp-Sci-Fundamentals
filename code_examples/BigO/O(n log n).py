
# O(n log n)
def foo(x):
    """
    Since each time you are cutting the list in half, each time you call foo, you are working with a list which is half the size of the one you just had. 
    Therefore, it takes O(log n) steps to reach the base case.

    The next question is: how much work is done at each step? 
    In the first step, the list is broken in half, which requires n memory copies. 
    In the second step, two lists of size n/2 are broken in half. 
    
    The amount of work done remains the same! From one step to the next, the size of each list you are cutting halves (due to calling foo(n//2)), but the number of lists you must do this for doubles (since you are calling foo twice recursively). 
    Therefore, for each step, you are always doing O(n) work.

    O(log n) steps * O(n) work at each step = O(n log n) in total.
    """
    n = len(x)
    if n <= 1:
        return 100
    return foo(x[:n//2]) + foo(x[n//2:])