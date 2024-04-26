def get_max_min_values(dictionary):
    if len(dictionary) == 0:
        print("The dictionary is empty.")
        return None, None
    max_value = max(dictionary.values())  # najwyższa wartość ze słownika
    min_value = min(dictionary.values())  # najmniejsza wartość ze słownika
    return max_value, min_value
# Test
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 40}
max_value, min_value = get_max_min_values(my_dict)
if max_value is not None and min_value is not None:
    print("Maximum value in the dictionary:", max_value)
    print("Minimum value in the dictionary:", min_value)
