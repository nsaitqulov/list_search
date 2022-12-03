def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 1
    a = data[0]
    while i < len(data):
        if a < data[i]:
            a = data[i]
        i += 1
    return data.index(a)
print(find_max_index([6, 8, 7, 4, 0]))
