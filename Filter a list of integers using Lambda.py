#### 19th Feb

## https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-5.php

# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list:
# [2, 4, 6, 8, 10]

# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

list__ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_filter = list(filter(lambda x: x % 2 == 0, list__))

print(f' even_filtered list is ', even_filter)  #  even_filtered list is  [2, 4, 6, 8, 10]


odd_filter = list(filter(lambda x: x % 2 == 1, list__))

print(f' Odd_filtered list is ', odd_filter)        #  Odd_filtered list is  [1, 3, 5, 7, 9]


