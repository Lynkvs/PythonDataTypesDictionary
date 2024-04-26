def is_dict_empty(dictionary):
    if not dictionary:  # Sprawdza czy słownik jest pusty
        print("The dictionary is empty.")
        return True
    else:
        print("The dictionary is not empty.")
        return False
# Test
empty_dict = {}
non_empty_dict = {'test': 1, 'dawno': 2}
is_dict_empty(empty_dict)
is_dict_empty(non_empty_dict)
