def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i = 0
    a = []
    while i < len(data):
        if data[i] % 2 == 1:
            a.append(data[i])
        i += 1

    x = 1
    b = a[0]
    while x <len(a):
        if b > a[x]:
            b = a[x]
        x += 1
    return b
print(find_min_odd([7, 8, 4, 3, 5]))

