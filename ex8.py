def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # kopiowanie 1 słownika
    merged_dict.update(dict2)   # łączenie 2 słownika z 1
    return merged_dict

# Test:
dict1 = {'f': 3, 's': 9}
dict2 = {'c': 3, 'd': 4}

merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)
