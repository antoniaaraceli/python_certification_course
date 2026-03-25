# Build a User Configuration Manager

def add_setting(dictionary, tuple):
    key, value = tuple
    key = key.lower()
    value = value.lower() if isinstance(value, str) else value # Prevents typeError when value is not a string
    
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
    
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, tuple):
    key, value = tuple
    key = key.lower()
    value = value.lower() if isinstance(value, str) else value

    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."    

def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary):
    output = ''
    if len(dictionary) == 0:
        return f"No settings available."
    else:
        for key, value in dictionary.items():
            key = key.capitalize()
            output += key + ': ' + value + '\n'
            #print(key, value)
        return f"Current User Settings:\n{output}"


## TEST CASES
test_settings = {"theme": "dark", "language": "spanish", "volume": "high"}
# print(add_setting(test_settings, ("FONT-size", 15)))
# print(add_setting(test_settings, ("theme", 14)))
# print(update_setting(test_settings,("theme", "wHite")))
# print(delete_setting(test_settings, 'Theme'))
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
# print(test_settings)
