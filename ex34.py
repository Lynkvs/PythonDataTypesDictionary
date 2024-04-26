def count_list_items(dictionary):
    count = 0  # Inicjalizacja licznika elementów listy
    for value in dictionary.values():
        if isinstance(value, list):  # Sprawdź, czy wartość jest listą
            count += len(value)  # Zwiększa licznik o długość listy
    return count

# Test:
my_dict = {'d': [6, 1, 3], 'g': 'not a list', 'c': [4, 5]}

list_item_count = count_list_items(my_dict)
print("Number of items in dictionary values that are lists:", list_item_count)
