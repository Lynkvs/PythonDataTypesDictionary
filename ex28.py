def sort_list_alphabetically(dictionary):
    sorted_dict = {key: sorted(value) for key, value in dictionary.items()}
    return sorted_dict

# Test
my_dict = {'pojazdy': ['rower', 'samolot', 'samochód'], 'kolory': ['czarny', 'fiolet', 'zielony']}

sorted_dict = sort_list_alphabetically(my_dict)
print("Sorted dictionary with lists sorted alphabetically:", sorted_dict)
