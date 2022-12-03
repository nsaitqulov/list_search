def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i = 0
    a = data[0]
    while i < len(data):
        if a > data[i]:
            a = data[i]
        i += 1
    return a
print(find_min([15, 23, 3, 9, 1, 4]))