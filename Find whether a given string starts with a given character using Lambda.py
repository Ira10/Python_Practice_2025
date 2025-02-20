#### 19th Feb

### https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-7.php


# Let's break this down step by step.

# ### 1. **Defining the Lambda Function**
# ```python
# starts_with = lambda x: True if x.startswith('P') else False
# ```
# - This defines a **lambda function** named `starts_with`.
# - `lambda x:` means it takes a single argument `x`.
# - `x.startswith('P')` checks if the string `x` starts with the letter `'P'`.
# - The `True if ... else False` part is unnecessary here because `x.startswith('P')` already returns `True` or `False`. A simpler version of this lambda would be:
#   ```python
#   starts_with = lambda x: x.startswith('P')
#   ```

# ---

# ### 2. **Checking If 'Python' Starts with 'P'**
# ```python
# print(starts_with('Python'))
# ```
# - `'Python'.startswith('P')` → **True**
# - So, `print(starts_with('Python'))` prints:
#   ```
#   True
#   ```

# ---

# ### 3. **Checking If 'Java' Starts with 'P'**
# ```python
# print(starts_with('Java'))
# ```
# - `'Java'.startswith('P')` → **False**
# - So, `print(starts_with('Java'))` prints:
#   ```
#   False
#   ```

# ---

# ### 4. **Redefining the Lambda Function**
# ```python
# starts_with = lambda x: True if x.startswith('P') else False
# ```
# - This redefinition is identical to the first one. It does **not** change the functionality.
# - The function still checks if a string starts with `'P'`.

# ### **Final Output of the Code**
# ```
# True
# False
# ```
# Would you like me to simplify or improve this code? 😊

# Define a lambda function 'starts_with' that checks if a given string starts with 'P'
starts_with = lambda x: True if x.startswith('P') else False

# Check if the string 'Python' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Python'))

# Redefine the lambda function 'starts_with' (same as before) to check if a string starts with 'P'
# Check if the string 'Java' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Java')) 


# True
# False
