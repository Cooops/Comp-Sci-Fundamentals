# O(n^2)
def all_combinations(array):
    """
    This function (algorithm) is considered O(n^2), as every input requires us to do n more operations.
    We have to iterate over each item in the array, and then each inner_item in the array.
    This creates two O(n) based steps (the time to iterate over them will depend on the input size, n).
    
    O(n) steps * O(n) steps == O(n^2) in total.
    """
    results = []
    for item in array:
        for inner_item in array:
            results.append((item, inner_item))
    return results