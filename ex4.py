def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")
# Test:
new_dict = {'a': 1, 'b': 2, 'h': 3}
check_key(new_dict, 'g')  #  The key 'a' istnieje w słowniku
check_key(new_dict, 'h')  #  The key 'd' nie istnieje w słowniku
