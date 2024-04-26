def check_all_values(dictionary, value):
    # Iteruj wartości słownika
    for val in dictionary.values():
        # Jeśli jakakolwiek wartość nie jest równa podanej wartości, zwraca False
        if val != value:
            return False
    # Jeśli wszystkie wartości są równe podanej wartości, zwracana jest wartość True
    return True
# Original Dictionary
original_dict = {'Lucas': 12, 'Robert': 12, 'Smith': 12, 'Jake': 12}
# Check all values are 12 in the dictionary
print("Check all are 12 in the dictionary:")
print(check_all_values(original_dict, 12))
# Check all values are 10 in the dictionary
print("Check all are 10 in the dictionary:")
print(check_all_values(original_dict, 10))
