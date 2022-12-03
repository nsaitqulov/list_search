def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    a = []
    while i < len(data):
        if data[i] % 2 == 0:
            a.append(data[i])
        i += 1
    
    ix = 1
    b = a[0]
    while ix < len(a):
        if b < a[ix]:
            b = a[ix]
        ix += 1
    return b
print(find_max_even([1, 4, 3, 8, 5]))
        


