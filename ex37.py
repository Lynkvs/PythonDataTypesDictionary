def replace_with_sum(dictionary):
    for key in dictionary:
        # If the value is a list or tuple, calculate its sum
        if isinstance(dictionary[key], (list, tuple)):
            dictionary[key] = sum(dictionary[key])
    return dictionary
# Test
my_dict = {'g': [3, 4, 3], 'b': (2, 5, 6), 'c': 10}

updated_dict = replace_with_sum(my_dict)
print("Updated Dictionary with values replaced with their sums:", updated_dict)
