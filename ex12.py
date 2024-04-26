def remove_key_using_del(dictionary, key):
    if key in dictionary:  # Sprawdza czy key istnieje w słowniku
        del dictionary[key]  # usuwa key ze słownika
        print(f"The key '{key}' has been removed from the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")
# Test:
my_dict = {'x': 1, 'y': 25, 'z': 23}
remove_key_using_del(my_dict, 'b')
print("Dictionary after using del:", my_dict)  
