def swap(d):
    if len(d) != len(set(d.values())):
        return None
    swapped = {v: k for k, v in d.items()}
    return swapped

dict = {'a': 1, 'b': 2, 'c': 3}
print(swap(dict))
