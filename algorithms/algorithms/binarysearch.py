

def binary_search(array, element):
    """
    Uses binary search to determine if a given element is in a sorted array.
    :param array: list
    :param element: int element
    :return: Boolean: Bool True if element is in the array else False
    """
    length = len(array)
    midpoint = length//2

    if length == 1:
        return True if array[0] == element else False
    elif length == 0:
        return False
    elif length == 2:
        next_half = array[:1] if array[midpoint] > element else array[1:]
    else:
        next_half = array[ :midpoint + 1 ] if array[midpoint] >= element \
        else array[midpoint:]
    return  binary_search(next_half, element)