def multiply_dictionary(dictionary):
    result = 1  # Inicjalizacja zmiennej do przechowywania wyniku mnożenia
    for value in dictionary.values():  # Iteruje każdy wyraz w słowniku
        result *= value  # mnożenie
    return result

# Example usage:
my_dict = {'z': 45, 'y': 3, 'x': 4}

total_product = multiply_dictionary(my_dict)  # Wywołanie funkcji mnożącej wszystkie wartości w słowniku
print("Product of all items in the dictionary:", total_product)
