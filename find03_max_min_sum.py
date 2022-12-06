def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 1
    a = data[0]
    while i < len(data):
        if a < data[i]:
            a = data[i]
        i += 1
    b = data[0]
    while i < len(data):
        if b > data[i]:
            b = data[i]
        
    return a + b
print(find_max_min_sum([2, 7, 3, 4, 9, 12]))