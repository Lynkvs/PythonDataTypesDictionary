def remove_spaces_from_keys(dictionary):
    new_dict = {}  # Utwórz pusty słownik do przechowywania par klucz-wartość z usuniętymi spacjami z kluczy.
    for key, value in dictionary.items():
        new_key = key.strip()  # Usuń spacje z klucza za pomocą funkcji strip()
        new_dict[new_key] = value  # Dodanie pary klucz-wartość do nowego słownika
    return new_dict

# Test:
my_dict = {'  pok   ': 1, ' dec    ': 2, 'ex   ': 3}
new_dict = remove_spaces_from_keys(my_dict)
print("Dictionary with spaces removed from keys:", new_dict)
