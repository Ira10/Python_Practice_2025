## 17th Feb

### https://www.w3resource.com/python-exercises/python-functions-exercise-14.php

# Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Import the 'string' and 'sys' modules
import string
import sys

# Define a function named 'ispangram' that checks if a string is a pangram
def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set 'alphaset' containing all lowercase letters from the provided alphabet
    alphaset = set(alphabet)
    print(f'alphaset is', alphaset)
    
    # Convert the input string to lowercase and create a set from it
    str_set = set(str1.lower())
    print(f'str_ is', str_set)
    
    # Check if the set of lowercase characters in the input string covers all characters in 'alphaset'
    return alphaset <= str_set

# Print the result of checking if the string is a pangram by calling the 'ispangram' function
print(ispangram('The quick brown fox jumps over the lazy dog'))  # True
# print(set(string.ascii_letters))
