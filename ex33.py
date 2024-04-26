def check_multiple_keys_exist(dictionary, keys):
    # Iteruj każdy wyraz w kluczu
    for key in keys:
        if key not in dictionary:
            return False
    return True
# Test:
my_dict = {'g': 1, 'h': 2, 'c': 3}
keys_to_check = ['g', 'h', 'c']
if check_multiple_keys_exist(my_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("At least one key does not exist in the dictionary.")
