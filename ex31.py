def print_dictionary_items(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")

# Test:
my_dict = {'g': 1, 'h': 4, 'c': 3}

print("Printing key, value, and item in the dictionary:")
print_dictionary_items(my_dict)
