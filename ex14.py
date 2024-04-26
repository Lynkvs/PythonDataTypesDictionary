def sort_dictionary_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))  # Sortuje słownik za pomocy key i konweruje
    return sorted_dict

# Test:
my_dict = {'f': 2, 'd': 3, 'c': 1}
sorted_dict = sort_dictionary_by_key(my_dict)
print("Sorted dictionary by key:", sorted_dict)
