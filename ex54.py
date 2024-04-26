def get_dictionary_depth(dictionary):
    #  jeśli słownik nie jest zagnieżdżony, zwróć 1
    if not isinstance(dictionary, dict):
        return 1
    # inicjalizacja scieżki na 1
    depth = 1
    # Iteruj przez wyrazy słownika
    for value in dictionary.values():
        # Znajduje zagniezdzony słownik
        if isinstance(value, dict):
            depth = max(depth, 1 + get_dictionary_depth(value))
    return depth
# Test
my_dict = {'a': {'b': {'c': {'d': 5}}}, 'e': 6, 'f': {'g': 7}}

depth = get_dictionary_depth(my_dict)
print("Orginal dictionary",my_dict)
print("Depth of the dictionary:", depth)
