def print_dictionary_line_by_line(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
# Test:
my_dict = {'dawno': 1, 'temu': 2, 'za': 3}
print("Printing dictionary line by line:")
print_dictionary_line_by_line(my_dict)
