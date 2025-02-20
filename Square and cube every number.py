#### 19th Feb

## https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-6.php

list__ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square__ = list(map(lambda x: x * x, list__))       ##      x**2

print(f' square list is ', square__)  #   square list is  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


cube__ = list(map(lambda x: x**3, list__))

print(f' cube list is ', cube__)        #   cube list is  [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]