###### 19th Feb 

## https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-4.php#google_vignette

# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


# Create a list of dictionaries named 'models', each dictionary representing a mobile phone model with 'make', 'model', and 'color' keys
models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Display a message indicating that the following output will show the original list of dictionaries
print("Original list of dictionaries:")
print(models)
# print(models['color'])  # You cannot access a list using a string key like models['color'] because models is a list of dictionaries, not a dictionary itself. Instead, you need to iterate over the list and extract the 'color' value from each dictionary.
# for phone in models:
#     print(phone['color'])

# Sort the list of dictionaries ('models') based on the value associated with the 'color' key in each dictionary
# Uses the 'sorted()' function with a lambda function as the sorting key to sort based on the 'color' value
sorted_models = sorted(models, key=lambda x: x['color'])


# Display a message indicating that the following output will show the sorted list of dictionaries
print("\nSorting the List of dictionaries:")
print(sorted_models) 

