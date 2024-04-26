def sum_dictionary(dictionary):
    total = 0 # Inicjalizacja zmiennej do przechowywania sumy wszystkich wartości
    for value in dictionary.values():
        total += value # Dodaj każdą wartość do sumy całkowitej
    return total

# Test
first_dict = {'a': 32, 'b': 0, 'c': 6}

total_sum = sum_dictionary(first_dict)
print("Sum of all items in the dictionary:", total_sum)
