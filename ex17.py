def remove_duplicates(dictionary):
    unique_dict = {}  # Tworzy pusty słownik do przechowywania unikalnych par klucz-wartość
    for key, value in dictionary.items():  # Iteruje każdy wyraz w słowniku
        if value not in unique_dict.values():  # Sprawdź, czy wartość jest już  w unikalnym słowniku.
            unique_dict[key] = value  # Jeśli nie istnieje, dodaj parę klucz-wartość do unikalnego słownika.
    return unique_dict

# Test
my_dict = {'c': 1, 'f': 2, 'c': 1, 'd': 3, 'e': 2}

unique_dict = remove_duplicates(my_dict)
print("Dictionary after removing duplicates:", unique_dict)
